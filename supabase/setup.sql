-- Execute no SQL Editor do Supabase (https://supabase.com/dashboard)
-- Projeto → SQL → New query → Run

create table if not exists public.plano_notes (
  id uuid primary key default gen_random_uuid(),
  item_id text not null,
  ts timestamptz not null default now(),
  ts_br text,
  user_name text,
  text text not null,
  created_at timestamptz not null default now()
);

create index if not exists plano_notes_item_id_idx on public.plano_notes (item_id);
create index if not exists plano_notes_ts_idx on public.plano_notes (ts);

alter table public.plano_notes enable row level security;

drop policy if exists "plano_notes_select" on public.plano_notes;
drop policy if exists "plano_notes_insert" on public.plano_notes;
drop policy if exists "plano_notes_delete" on public.plano_notes;

create policy "plano_notes_select"
  on public.plano_notes for select
  using (true);

create policy "plano_notes_insert"
  on public.plano_notes for insert
  with check (true);

create policy "plano_notes_delete"
  on public.plano_notes for delete
  using (true);

alter publication supabase_realtime add table public.plano_notes;

-- Log de atividades compartilhado
create table if not exists public.plano_log (
  id uuid primary key default gen_random_uuid(),
  ts timestamptz not null default now(),
  ts_br text,
  type text not null,
  item_id text default '',
  details text default '',
  user_name text,
  browser text,
  created_at timestamptz not null default now()
);

create index if not exists plano_log_ts_idx on public.plano_log (ts desc);

alter table public.plano_log enable row level security;

drop policy if exists "plano_log_select" on public.plano_log;
drop policy if exists "plano_log_insert" on public.plano_log;
drop policy if exists "plano_log_delete" on public.plano_log;

create policy "plano_log_select"
  on public.plano_log for select
  using (true);

create policy "plano_log_insert"
  on public.plano_log for insert
  with check (true);

create policy "plano_log_delete"
  on public.plano_log for delete
  using (true);

alter publication supabase_realtime add table public.plano_log;

-- Conclusões marcadas compartilhadas
create table if not exists public.plano_state (
  item_id text primary key,
  completed boolean not null default true,
  completed_at timestamptz,
  completed_by text,
  updated_at timestamptz not null default now()
);

alter table public.plano_state enable row level security;

drop policy if exists "plano_state_select" on public.plano_state;
drop policy if exists "plano_state_insert" on public.plano_state;
drop policy if exists "plano_state_update" on public.plano_state;
drop policy if exists "plano_state_delete" on public.plano_state;

create policy "plano_state_select"
  on public.plano_state for select
  using (true);

create policy "plano_state_insert"
  on public.plano_state for insert
  with check (true);

create policy "plano_state_update"
  on public.plano_state for update
  using (true) with check (true);

create policy "plano_state_delete"
  on public.plano_state for delete
  using (true);

alter publication supabase_realtime add table public.plano_state;

-- Ações personalizadas criadas pelo botão "Nova ação"
create table if not exists public.plano_custom_actions (
  id text primary key,
  title text not null,
  resp jsonb not null default '[]',
  deadline date not null,
  created_by text,
  created_at timestamptz not null default now()
);

create index if not exists plano_custom_actions_created_idx on public.plano_custom_actions (created_at);

alter table public.plano_custom_actions enable row level security;

drop policy if exists "plano_custom_actions_select" on public.plano_custom_actions;
drop policy if exists "plano_custom_actions_insert" on public.plano_custom_actions;
drop policy if exists "plano_custom_actions_update" on public.plano_custom_actions;
drop policy if exists "plano_custom_actions_delete" on public.plano_custom_actions;

create policy "plano_custom_actions_select"
  on public.plano_custom_actions for select
  using (true);

create policy "plano_custom_actions_insert"
  on public.plano_custom_actions for insert
  with check (true);

create policy "plano_custom_actions_update"
  on public.plano_custom_actions for update
  using (true) with check (true);

create policy "plano_custom_actions_delete"
  on public.plano_custom_actions for delete
  using (true);

alter publication supabase_realtime add table public.plano_custom_actions;
