const SUPABASE_URL = "https://bpxiuegqhxhuofyiyujq.supabase.co";
const SUPABASE_KEY = "sb_publishable_9q6pLEPJ3DmbWhNVm2IRHQ_f9_eojBD";
const REPLACE_USER = "Antonio Rodrigues";

const data = {
  exportedAt: "2026-07-11T16:18:09.102Z",
  state: {
    "3": { completed: true, completedAt: "2026-07-07T15:35:25.027Z", completedBy: "(sem nome)" },
    "16": { completed: true, completedAt: "2026-07-07T20:36:57.104Z", completedBy: "Antonio Rodrigues" },
    "21": { completed: true, completedAt: "2026-07-07T16:06:35.492Z", completedBy: "Antonio Rodrigues" },
    M1: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M2: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M3: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M4: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M5: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M6: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M7: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M8: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M9: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M11: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M12: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M13: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M14: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M15: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M17: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    M18: { completed: true, completedAt: "2026-07-02T12:00:00.000Z", completedBy: "Registro histórico (CSV Melhorias)" },
    "1.1": { completed: true, completedAt: "2026-07-07T15:21:29.821Z", completedBy: "(sem nome)" },
    "1.2": { completed: true, completedAt: "2026-07-07T16:04:12.224Z", completedBy: "Antonio Rodrigues" },
  },
  log: [
    { ts: "2026-07-07T20:36:57.104Z", tsBR: "07/07/2026 17:36:57", type: "done", itemId: "16", details: 'Concluída: "Enviar e-mail ao setor de Suprimentos solicitando orçamento para instalação de c…"', user: "Antonio Rodrigues", browser: "Chrome · macOS" },
    { ts: "2026-07-07T16:06:35.492Z", tsBR: "07/07/2026 13:06:35", type: "done", itemId: "21", details: 'Concluída: "Enviar e-mail ao RH informando a necessidade de contratação de um responsável em…"', user: "Antonio Rodrigues", browser: "Chrome · macOS" },
    { ts: "2026-07-07T16:06:34.226Z", tsBR: "07/07/2026 13:06:34", type: "note", itemId: "21", details: 'Anotação em 21 ("Enviar e-mail ao RH informando a necessidade de co…"): "E-mail enviado!\nAntonio enviou em 07/07/2026 - A ordem de prioridades dos esta…"', user: "Antonio Rodrigues", browser: "Chrome · macOS" },
    { ts: "2026-07-07T16:04:12.224Z", tsBR: "07/07/2026 13:04:12", type: "done", itemId: "1.2", details: 'Concluída: "Definir responsável do Controle de Qualidade"', user: "Antonio Rodrigues", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:35:43.917Z", tsBR: "07/07/2026 12:35:43", type: "user", itemId: "", details: 'Nome alterado de "(vazio)" para "Antonio Rodrigues"', user: "Antonio Rodrigues", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:35:25.027Z", tsBR: "07/07/2026 12:35:25", type: "done", itemId: "3", details: 'Concluída: "Descontinuar uso da antecâmara de −7 °C"', user: "(sem nome)", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:35:23.859Z", tsBR: "07/07/2026 12:35:23", type: "note", itemId: "3", details: 'Anotação em 3 ("Descontinuar uso da antecâmara de −7 °C"): "Definido com o Rogério e William no dia do prazo."', user: "(sem nome)", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:21:44.401Z", tsBR: "07/07/2026 12:21:44", type: "note", itemId: "1.2", details: 'Anotação em 1.2 ("Definir responsável do Controle de Qualidade"): "Diurno:\nPaulo Roberto"', user: "(sem nome)", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:21:29.821Z", tsBR: "07/07/2026 12:21:29", type: "done", itemId: "1.1", details: 'Concluída: "Definir responsável do processo de movimentação de gaiolas de gelox"', user: "(sem nome)", browser: "Chrome · macOS" },
    { ts: "2026-07-07T15:21:26.932Z", tsBR: "07/07/2026 12:21:26", type: "note", itemId: "1.1", details: 'Anotação em 1.1 ("Definir responsável do processo de movimentação de…"): "Diurno: \nADM: João Ribeiro\nOP: Diego Teixeira\n\nNoturno:\nADM: Anderson Sansini\n…"', user: "(sem nome)", browser: "Chrome · macOS" },
  ],
  notes: {
    "3": [{ ts: "2026-07-07T15:35:23.858Z", tsBR: "07/07/2026 12:35:23", user: "(sem nome)", text: "Definido com o Rogério e William no dia do prazo." }],
    "21": [{ ts: "2026-07-07T16:06:34.226Z", tsBR: "07/07/2026 13:06:34", user: "Antonio Rodrigues", text: "E-mail enviado!\nAntonio enviou em 07/07/2026 - A ordem de prioridades dos estados para o RH: PR/CE/AM/SE/RN" }],
    "1.1": [{ ts: "2026-07-07T15:21:26.932Z", tsBR: "07/07/2026 12:21:26", user: "(sem nome)", text: "Diurno: \nADM: João Ribeiro\nOP: Diego Teixeira\n\nNoturno:\nADM: Anderson Sansini\nOP: Pedro Santiago" }],
    "1.2": [{ ts: "2026-07-07T15:21:44.401Z", tsBR: "07/07/2026 12:21:44", user: "(sem nome)", text: "Diurno:\nPaulo Roberto" }],
  },
};

function fixUser(name) {
  return !name || name === "(sem nome)" ? REPLACE_USER : name;
}

async function sb(path, { method = "GET", body, prefer } = {}) {
  const headers = {
    apikey: SUPABASE_KEY,
    Authorization: `Bearer ${SUPABASE_KEY}`,
    "Content-Type": "application/json",
  };
  if (prefer) headers.Prefer = prefer;
  const res = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, { method, headers, body: body ? JSON.stringify(body) : undefined });
  const text = await res.text();
  if (!res.ok) throw new Error(`${method} ${path} → ${res.status}: ${text}`);
  return text ? JSON.parse(text) : null;
}

async function main() {
  // --- STATE ---
  const stateRows = Object.entries(data.state).map(([id, s]) => ({
    item_id: id,
    completed: true,
    completed_at: s.completedAt,
    completed_by: fixUser(s.completedBy),
    updated_at: new Date().toISOString(),
  }));
  const stateRes = await sb("plano_state?on_conflict=item_id", { method: "POST", body: stateRows, prefer: "resolution=merge-duplicates,return=representation" });
  console.log(`✅ Conclusões: ${stateRes.length} itens upsertados`);

  // --- LOG (dedup por ts+type+item_id+user) ---
  const existingLog = await sb("plano_log?select=ts,type,item_id,user_name");
  const seenLog = new Set(existingLog.map(e => `${e.ts}|${e.type}|${e.item_id}|${e.user_name}`));
  const logRows = data.log
    .map(e => ({
      ts: e.ts,
      ts_br: e.tsBR,
      type: e.type,
      item_id: e.itemId || "",
      details: e.details,
      user_name: fixUser(e.user),
      browser: e.browser,
    }))
    .filter(e => {
      const k = `${e.ts}|${e.type}|${e.item_id}|${e.user_name}`;
      if (seenLog.has(k)) return false;
      seenLog.add(k);
      return true;
    });
  if (logRows.length) {
    const logRes = await sb("plano_log", { method: "POST", body: logRows, prefer: "return=representation" });
    console.log(`✅ Log: ${logRes.length} entradas inseridas (${data.log.length - logRows.length} já existiam)`);
  } else {
    console.log("✅ Log: nenhuma entrada nova (todas já existiam)");
  }

  // --- NOTES (dedup por ts+user por item) ---
  const existingNotes = await sb("plano_notes?select=item_id,ts,user_name");
  const seenNotes = new Set(existingNotes.map(e => `${e.item_id}|${e.ts}|${e.user_name}`));
  const noteRows = [];
  for (const [itemId, list] of Object.entries(data.notes)) {
    for (const n of list) {
      const user = fixUser(n.user);
      const k = `${itemId}|${n.ts}|${user}`;
      if (seenNotes.has(k)) continue;
      seenNotes.add(k);
      noteRows.push({ item_id: itemId, ts: n.ts, ts_br: n.tsBR, user_name: user, text: n.text });
    }
  }
  if (noteRows.length) {
    const notesRes = await sb("plano_notes", { method: "POST", body: noteRows, prefer: "return=representation" });
    console.log(`✅ Anotações: ${notesRes.length} inseridas`);
  } else {
    console.log("✅ Anotações: nenhuma nova (todas já existiam)");
  }

  // resumo final
  for (const t of ["plano_state", "plano_log", "plano_notes"]) {
    const rows = await sb(`${t}?select=*`);
    console.log(`   ${t}: ${rows.length} registros no total`);
  }
}

main().catch(err => { console.error("❌ Erro:", err.message); process.exit(1); });
