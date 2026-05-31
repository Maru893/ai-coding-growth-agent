from pathlib import Path


def export_weekly_plan_to_markdown(plan, export_dir="exports"):
    Path(export_dir).mkdir(parents=True, exist_ok=True)

    focus = plan.get("focus", "piano").lower().replace(" ", "-")
    file_path = Path(export_dir) / f"weekly-plan-{focus}.md"

    content = f"""# Piano settimanale

## Informazioni generali

- Ore disponibili: {plan.get("hours", "Non impostato")}
- Energia mentale: {plan.get("energy", "Non impostata")}
- Focus: {plan.get("focus", "Non impostato")}
- Obiettivo: {plan.get("goal", "Non impostato")}
- Progetto attuale: {plan.get("current_project", "Non impostato")}

## Distribuzione tempo

- Studio: {plan.get("plan", {}).get("study", "Non impostato")}
- Pratica: {plan.get("plan", {}).get("practice", "Non impostato")}
- Documentazione: {plan.get("plan", {}).get("documentation", "Non impostato")}
- Difficoltà: {plan.get("plan", {}).get("difficulty", "Non impostata")}
- Tipo task: {plan.get("plan", {}).get("task_type", "Non impostato")}

## Task tecnico

{plan.get("plan", {}).get("technical_task", "Non impostato")}

## Checklist

"""

    for item in plan.get("checklist", []):
        content += f"- [ ] {item}\n"

    content += f"""

## Output GitHub

{plan.get("github_output", "Non impostato")}

## Possibile uso monetizzabile

{plan.get("money_path", "Non impostato")}

## Raccomandazione skill

{plan.get("skill_recommendation", "Non impostata")}

## Focus settimanale collegato

{plan.get("weekly_focus_recommendation", "Non impostato")}
"""


    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return file_path