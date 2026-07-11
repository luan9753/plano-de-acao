#!/usr/bin/env python3
"""Migra os item_id antigos (M1, 1.1, 28.1, ...) para a nova sequência 1..56
nas tabelas plano_state, plano_notes e plano_log do Supabase."""
import json
import re
import urllib.request

SUPABASE_URL = "https://bpxiuegqhxhuofyiyujq.supabase.co"
SUPABASE_KEY = "sb_publishable_9q6pLEPJ3DmbWhNVm2IRHQ_f9_eojBD"
MARKER = "__SEEDED__"

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
    """Troca referências textuais 'em {old} (' por 'em {new} (' no log de anotações."""
    if not details or not old:
        return details
    return re.sub(r'(?<=em )' + re.escape(old) + r'(?= \()', new, details)


def migrate_state():
    rows = sb("plano_state?select=*")
    keep = [r for r in rows if r["item_id"] != MARKER]
    # apaga todas as linhas exceto o marcador de seed
    sb(f"plano_state?item_id=neq.{MARKER}", method="DELETE", prefer="return=minimal")
    new_rows = []
    for r in keep:
        new_rows.append({
            "item_id": new_id(r["item_id"]),
            "completed": r.get("completed", True),
            "completed_at": r.get("completed_at"),
            "completed_by": r.get("completed_by"),
            "updated_at": "2026-07-11T18:00:00.000Z",
        })
    if new_rows:
        sb("plano_state?on_conflict=item_id", method="POST", body=new_rows,
           prefer="resolution=merge-duplicates,return=minimal")
    changed = sum(1 for r in keep if r["item_id"] in MAP)
    print(f"✅ Conclusões: {len(keep)} linhas reinseridas ({changed} com ID remapeado)")


def migrate_notes():
    rows = sb("plano_notes?select=id,item_id")
    n = 0
    for r in rows:
        old = r["item_id"]
        nv = new_id(old)
        if nv != old:
            sb(f"plano_notes?id=eq.{r['id']}", method="PATCH", body={"item_id": nv}, prefer="return=minimal")
            n += 1
    print(f"✅ Anotações: {n} de {len(rows)} com ID remapeado")


def migrate_log():
    rows = sb("plano_log?select=id,item_id,details,type")
    n = 0
    for r in rows:
        old = r.get("item_id") or ""
        nv = new_id(old)
        new_details = remap_details(r.get("details"), old, nv) if old else r.get("details")
        patch = {}
        if nv != old:
            patch["item_id"] = nv
        if new_details != r.get("details"):
            patch["details"] = new_details
        if patch:
            sb(f"plano_log?id=eq.{r['id']}", method="PATCH", body=patch, prefer="return=minimal")
            n += 1
    print(f"✅ Log: {n} de {len(rows)} entradas atualizadas")


def main():
    migrate_state()
    migrate_notes()
    migrate_log()
    print("\n📊 Estado final:")
    for table in ["plano_state", "plano_notes", "plano_log"]:
        rows = sb(f"{table}?select=item_id")
        ids = sorted({r["item_id"] for r in rows if r["item_id"] != MARKER})
        print(f"   {table}: {len(rows)} registros | item_ids: {ids}")


if __name__ == "__main__":
    main()
