#!/usr/bin/env python3
import json
import urllib.request

SUPABASE_URL = "https://bpxiuegqhxhuofyiyujq.supabase.co"
SUPABASE_KEY = "sb_publishable_9q6pLEPJ3DmbWhNVm2IRHQ_f9_eojBD"
REPLACE_USER = "Antonio Rodrigues"

DATA = {
  "state": {
    "3": {"completed": True, "completedAt": "2026-07-07T15:35:25.027Z", "completedBy": "(sem nome)"},
    "16": {"completed": True, "completedAt": "2026-07-07T20:36:57.104Z", "completedBy": "Antonio Rodrigues"},
    "21": {"completed": True, "completedAt": "2026-07-07T16:06:35.492Z", "completedBy": "Antonio Rodrigues"},
    "M1": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M2": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M3": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M4": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M5": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M6": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M7": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M8": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M9": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M11": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M12": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M13": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M14": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M15": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M17": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "M18": {"completed": True, "completedAt": "2026-07-02T12:00:00.000Z", "completedBy": "Registro histórico (CSV Melhorias)"},
    "1.1": {"completed": True, "completedAt": "2026-07-07T15:21:29.821Z", "completedBy": "(sem nome)"},
    "1.2": {"completed": True, "completedAt": "2026-07-07T16:04:12.224Z", "completedBy": "Antonio Rodrigues"},
  },
  "log": [
    {"ts": "2026-07-07T20:36:57.104Z", "tsBR": "07/07/2026 17:36:57", "type": "done", "itemId": "16", "details": 'Concluída: "Enviar e-mail ao setor de Suprimentos solicitando orçamento para instalação de c…"', "user": "Antonio Rodrigues", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T16:06:35.492Z", "tsBR": "07/07/2026 13:06:35", "type": "done", "itemId": "21", "details": 'Concluída: "Enviar e-mail ao RH informando a necessidade de contratação de um responsável em…"', "user": "Antonio Rodrigues", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T16:06:34.226Z", "tsBR": "07/07/2026 13:06:34", "type": "note", "itemId": "21", "details": 'Anotação em 21 ("Enviar e-mail ao RH informando a necessidade de co…"): "E-mail enviado!\nAntonio enviou em 07/07/2026 - A ordem de prioridades dos esta…"', "user": "Antonio Rodrigues", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T16:04:12.224Z", "tsBR": "07/07/2026 13:04:12", "type": "done", "itemId": "1.2", "details": 'Concluída: "Definir responsável do Controle de Qualidade"', "user": "Antonio Rodrigues", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:35:43.917Z", "tsBR": "07/07/2026 12:35:43", "type": "user", "itemId": "", "details": 'Nome alterado de "(vazio)" para "Antonio Rodrigues"', "user": "Antonio Rodrigues", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:35:25.027Z", "tsBR": "07/07/2026 12:35:25", "type": "done", "itemId": "3", "details": 'Concluída: "Descontinuar uso da antecâmara de −7 °C"', "user": "(sem nome)", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:35:23.859Z", "tsBR": "07/07/2026 12:35:23", "type": "note", "itemId": "3", "details": 'Anotação em 3 ("Descontinuar uso da antecâmara de −7 °C"): "Definido com o Rogério e William no dia do prazo."', "user": "(sem nome)", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:21:44.401Z", "tsBR": "07/07/2026 12:21:44", "type": "note", "itemId": "1.2", "details": 'Anotação em 1.2 ("Definir responsável do Controle de Qualidade"): "Diurno:\nPaulo Roberto"', "user": "(sem nome)", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:21:29.821Z", "tsBR": "07/07/2026 12:21:29", "type": "done", "itemId": "1.1", "details": 'Concluída: "Definir responsável do processo de movimentação de gaiolas de gelox"', "user": "(sem nome)", "browser": "Chrome · macOS"},
    {"ts": "2026-07-07T15:21:26.932Z", "tsBR": "07/07/2026 12:21:26", "type": "note", "itemId": "1.1", "details": 'Anotação em 1.1 ("Definir responsável do processo de movimentação de…"): "Diurno: \nADM: João Ribeiro\nOP: Diego Teixeira\n\nNoturno:\nADM: Anderson Sansini\n…"', "user": "(sem nome)", "browser": "Chrome · macOS"},
  ],
  "notes": {
    "3": [{"ts": "2026-07-07T15:35:23.858Z", "tsBR": "07/07/2026 12:35:23", "user": "(sem nome)", "text": "Definido com o Rogério e William no dia do prazo."}],
    "21": [{"ts": "2026-07-07T16:06:34.226Z", "tsBR": "07/07/2026 13:06:34", "user": "Antonio Rodrigues", "text": "E-mail enviado!\nAntonio enviou em 07/07/2026 - A ordem de prioridades dos estados para o RH: PR/CE/AM/SE/RN"}],
    "1.1": [{"ts": "2026-07-07T15:21:26.932Z", "tsBR": "07/07/2026 12:21:26", "user": "(sem nome)", "text": "Diurno: \nADM: João Ribeiro\nOP: Diego Teixeira\n\nNoturno:\nADM: Anderson Sansini\nOP: Pedro Santiago"}],
    "1.2": [{"ts": "2026-07-07T15:21:44.401Z", "tsBR": "07/07/2026 12:21:44", "user": "(sem nome)", "text": "Diurno:\nPaulo Roberto"}],
  },
}


def fix_user(name):
    return REPLACE_USER if not name or name == "(sem nome)" else name


def sb(path, method="GET", body=None, prefer=None):
    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/{path}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode()
        return json.loads(text) if text else None


def main():
    state_rows = [
        {"item_id": k, "completed": True, "completed_at": v["completedAt"], "completed_by": fix_user(v["completedBy"]), "updated_at": "2026-07-11T17:45:00.000Z"}
        for k, v in DATA["state"].items()
    ]
    res = sb("plano_state?on_conflict=item_id", method="POST", body=state_rows, prefer="resolution=merge-duplicates,return=representation")
    print(f"✅ Conclusões: {len(res)} itens upsertados")

    existing_log = sb("plano_log?select=ts,type,item_id,user_name")
    seen_log = {f"{e['ts']}|{e['type']}|{e['item_id']}|{e['user_name']}" for e in existing_log}
    log_rows = []
    for e in DATA["log"]:
        row = {"ts": e["ts"], "ts_br": e["tsBR"], "type": e["type"], "item_id": e["itemId"] or "", "details": e["details"], "user_name": fix_user(e["user"]), "browser": e["browser"]}
        k = f"{row['ts']}|{row['type']}|{row['item_id']}|{row['user_name']}"
        if k not in seen_log:
            seen_log.add(k)
            log_rows.append(row)
    if log_rows:
        res = sb("plano_log", method="POST", body=log_rows, prefer="return=representation")
        print(f"✅ Log: {len(res)} entradas inseridas")
    else:
        print("✅ Log: nenhuma entrada nova")

    existing_notes = sb("plano_notes?select=item_id,ts,user_name")
    seen_notes = {f"{e['item_id']}|{e['ts']}|{e['user_name']}" for e in existing_notes}
    note_rows = []
    for item_id, notes in DATA["notes"].items():
        for n in notes:
            user = fix_user(n["user"])
            k = f"{item_id}|{n['ts']}|{user}"
            if k in seen_notes:
                continue
            seen_notes.add(k)
            note_rows.append({"item_id": item_id, "ts": n["ts"], "ts_br": n["tsBR"], "user_name": user, "text": n["text"]})
    if note_rows:
        res = sb("plano_notes", method="POST", body=note_rows, prefer="return=representation")
        print(f"✅ Anotações: {len(res)} inseridas")
    else:
        print("✅ Anotações: nenhuma nova")

    for table in ["plano_state", "plano_log", "plano_notes"]:
        rows = sb(f"{table}?select=*")
        print(f"   {table}: {len(rows)} registros no total")


if __name__ == "__main__":
    main()
