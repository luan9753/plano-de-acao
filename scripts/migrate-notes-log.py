#!/usr/bin/env python3
"""Remapeia item_id em plano_notes e plano_log via DELETE + INSERT
(essas tabelas não têm política UPDATE no RLS, então PATCH é bloqueado).
NÃO mexe em plano_state (já migrado)."""
import json
import re
import urllib.request

SUPABASE_URL = "https://bpxiuegqhxhuofyiyujq.supabase.co"
SUPABASE_KEY = "sb_publishable_9q6pLEPJ3DmbWhNVm2IRHQ_f9_eojBD"

MAP = {
    "M1": "1", "M2": "2", "M3": "3", "M4": "4", "M5": "5", "M6": "6", "M7": "7",
    "M8": "8", "M9": "9", "M10": "10", "M11": "11", "M12": "12", "M13": "13",
    "M14": "14", "M15": "15", "M16": "16", "M17": "17", "M18": "18",
    "1.1": "19", "1.2": "20", "1.3": "21", "3": "22", "4": "23", "10": "24",
    "13.1": "25", "14": "26", "15": "27", "16": "28", "21": "29", "28": "30", "28.1": "31",
    "7": "32", "8": "33", "13.2": "34", "17": "35", "23": "36",
    "5.1": "37", "5.2": "38", "5.3": "39", "6": "40", "9": "41", "12": "42", "26": "43", "27": "44",
    "2": "45", "5": "46", "5.4": "47", "22": "48", "24": "49", "25": "50",
    "20": "51", "19": "52",
    "11.1": "53", "13.3": "54", "18": "55", "11.2": "56",
}
ANY_UUID = "00000000-0000-0000-0000-000000000000"


def sb(path, method="GET", body=None, prefer=None):
    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/{path}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode()
        return json.loads(text) if text else None


def new_id(old):
    return MAP.get(old, old)


def remap_details(details, old, new):
    if not details or not old:
        return details
    return re.sub(r'(?<=em )' + re.escape(old) + r'(?= \()', new, details)


def migrate_notes():
    rows = sb("plano_notes?select=*")
    new_rows = []
    for r in rows:
        new_rows.append({
            "item_id": new_id(r["item_id"]),
            "ts": r["ts"],
            "ts_br": r.get("ts_br"),
            "user_name": r.get("user_name"),
            "text": r["text"],
            "created_at": r.get("created_at"),
        })
    sb(f"plano_notes?id=neq.{ANY_UUID}", method="DELETE", prefer="return=minimal")
    if new_rows:
        sb("plano_notes", method="POST", body=new_rows, prefer="return=minimal")
    print(f"✅ Anotações: {len(new_rows)} reinseridas com IDs novos")


def migrate_log():
    rows = sb("plano_log?select=*")
    new_rows = []
    for r in rows:
        old = r.get("item_id") or ""
        nv = new_id(old)
        new_rows.append({
            "ts": r["ts"],
            "ts_br": r.get("ts_br"),
            "type": r["type"],
            "item_id": nv,
            "details": remap_details(r.get("details"), old, nv) if old else r.get("details"),
            "user_name": r.get("user_name"),
            "browser": r.get("browser"),
            "created_at": r.get("created_at"),
        })
    sb(f"plano_log?id=neq.{ANY_UUID}", method="DELETE", prefer="return=minimal")
    if new_rows:
        sb("plano_log", method="POST", body=new_rows, prefer="return=minimal")
    print(f"✅ Log: {len(new_rows)} reinseridas com IDs novos")


def main():
    migrate_notes()
    migrate_log()
    print("\n📊 Estado final:")
    for table in ["plano_state", "plano_notes", "plano_log"]:
        rows = sb(f"{table}?select=item_id")
        ids = sorted({r["item_id"] for r in rows if r["item_id"] not in ("__SEEDED__", "")},
                     key=lambda x: (len(x), x))
        print(f"   {table}: {len(rows)} registros | item_ids: {ids}")


if __name__ == "__main__":
    main()
