#!/usr/bin/env python3
"""routine.yaml + prompt.md から、RemoteTrigger (create/update) に渡す body JSON を生成する。

使い方:
  python3 scripts/render.py routines/weekly-ai-digest                 # prompt と基本項目のみ（update 向け）
  python3 scripts/render.py routines/weekly-ai-digest --current cur.json
      # `RemoteTrigger get` の結果 (cur.json) を土台に、prompt と基本項目だけ差し替えた完全な body を出す。
      # job_config は部分更新できないため、prompt を変える update ではこちらを使う。

出力は標準出力。Claude Code 上で RemoteTrigger の body にそのまま渡す。
"""
import argparse, json, pathlib, re, sys, uuid
import yaml

def load(dir_: pathlib.Path):
    cfg = yaml.safe_load((dir_ / "routine.yaml").read_text())
    prompt = (dir_ / "prompt.md").read_text().rstrip() + "\n"
    vars_ = cfg.get("vars") or {}
    def sub(m):
        key = m.group(1)
        if key not in vars_:
            sys.exit(f"prompt.md に未定義の変数 {{{{{key}}}}} があります。routine.yaml の vars に追加してください。")
        return str(vars_[key])
    prompt = re.sub(r"\{\{(\w+)\}\}", sub, prompt)
    return cfg, prompt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("routine_dir")
    ap.add_argument("--current", help="RemoteTrigger get の JSON。与えると job_config を丸ごと引き継いで prompt だけ差し替える")
    a = ap.parse_args()
    cfg, prompt = load(pathlib.Path(a.routine_dir))

    body = {
        "name": cfg["name"],
        "cron_expression": cfg["schedule"]["cron"],
        "enabled": cfg.get("enabled", True),
    }
    if a.current:
        cur = json.load(open(a.current))
        cur = cur.get("data", cur)
        job = cur["job_config"]
        job["ccr"]["session_context"]["model"] = cfg["model"]
        for ev in job["ccr"]["events"]:
            ev["data"]["message"] = {"role": "user", "content": prompt}
        body["job_config"] = job
    else:
        env = cfg.get("environment_id")
        if not env:
            sys.exit("--current なしで job_config を組むには routine.yaml に environment_id が必要です")
        body["job_config"] = {"ccr": {
            "environment_id": env,
            "session_context": {"model": cfg["model"], "allowed_tools": cfg.get("allowed_tools", [])},
            "events": [{"data": {"uuid": str(uuid.uuid4()), "session_id": "", "type": "user",
                                 "parent_tool_use_id": None,
                                 "message": {"role": "user", "content": prompt}}}],
        }}
        # connector_uuid が書かれているコネクタだけを body に含める（uuid なしの項目は説明用）
        conns = []
        for c in cfg.get("mcp_connections") or []:
            if not c.get("connector_uuid"):
                continue
            conn = {"connector_uuid": c["connector_uuid"], "name": c["name"], "url": c["url"]}
            if c.get("always_allow_tools"):
                conn["tool_policy_overrides"] = [
                    {"name": t, "permission_policy": "always_allow"} for t in c["always_allow_tools"]]
            conns.append(conn)
        if conns:
            body["mcp_connections"] = conns
    json.dump(body, sys.stdout, ensure_ascii=False, indent=2)
    print()

if __name__ == "__main__":
    main()
