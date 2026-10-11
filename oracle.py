#!/usr/bin/env python3
"""Oracle mirror of engine.js for Towel math. Writes expected.json (with trailing newline)."""
import json, math

def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100

def jsnum(x):
    if isinstance(x, float) and x == int(x) and abs(x) < 1e15:
        return int(x)
    return x

def fmt(x):
    if isinstance(x, float) and x == int(x):
        return str(int(x))
    return repr(x) if isinstance(x, float) else str(x)

def weightPlan(widthCm, heightCm, gsm):
    if not (widthCm > 0) or not (heightCm > 0) or not (gsm > 0):
        return {"error": "size and GSM must be positive"}
    grams = r1(widthCm * heightCm / 10000 * gsm)
    return {"widthCm": jsnum(float(widthCm)), "heightCm": jsnum(float(heightCm)), "gsm": jsnum(float(gsm)), "grams": jsnum(grams)}

def loadPlan(towelG, count, machineKg):
    if not (towelG > 0) or not (count > 0) or not (machineKg > 0):
        return {"error": "weight, count and capacity must be positive"}
    perLoad = math.floor(machineKg * 1000 / towelG)
    if perLoad < 1:
        return {"error": "one towel is heavier than the machine's labeled capacity"}
    loads = math.ceil(count / perLoad)
    return {"towelG": jsnum(float(towelG)), "count": jsnum(float(count)), "machineKg": jsnum(float(machineKg)),
            "perLoad": perLoad, "loads": loads}

def costPlan(loadsWeek, costPerLoad):
    if not (loadsWeek > 0) or not (costPerLoad > 0):
        return {"error": "loads and cost must be positive"}
    loadsYear = math.floor(loadsWeek * 52 + 0.5)
    costYear = r2(loadsYear * costPerLoad)
    return {"loadsWeek": jsnum(float(loadsWeek)), "costPerLoad": jsnum(float(costPerLoad)),
            "loadsYear": loadsYear, "costYear": jsnum(costYear)}

def renderWeight(r):
    return "A " + fmt(r["widthCm"]) + " x " + fmt(r["heightCm"]) + " cm towel at a labeled " + fmt(r["gsm"]) + " GSM weighs " + fmt(r["grams"]) + " g."

def renderLoad(r):
    return ("At " + fmt(r["towelG"]) + " g a towel, a labeled " + fmt(r["machineKg"]) + " kg machine takes " + str(r["perLoad"]) +
            " towels a load - " + fmt(r["count"]) + " towel" + ("" if r["count"] == 1 else "s") + " is " + str(r["loads"]) + " load" + ("" if r["loads"] == 1 else "s") + ".")

def renderCost(r):
    return (fmt(r["loadsWeek"]) + " loads a week at a labeled " + fmt(r["costPerLoad"]) + " a load is " + str(r["loadsYear"]) +
            " loads and about " + fmt(r["costYear"]) + " a year.")

CASES = []
CASES.append({"fn": "weightPlan", "args": [70, 140, 500]})
CASES.append({"fn": "weightPlan", "args": [50, 100, 450]})
CASES.append({"fn": "weightPlan", "args": [30, 30, 600]})
CASES.append({"fn": "weightPlan", "args": [100, 180, 400]})
CASES.append({"fn": "weightPlan", "args": [40, 70, 550]})
CASES.append({"fn": "weightPlan", "args": [90, 160, 350]})
CASES.append({"fn": "weightPlan", "args": [0, 140, 500]})
CASES.append({"fn": "weightPlan", "args": [70, 0, 500]})
CASES.append({"fn": "weightPlan", "args": [70, 140, 0]})
CASES.append({"fn": "weightPlan", "args": [35, 75, 700]})
CASES.append({"fn": "weightPlan", "args": [80, 160, 480]})
CASES.append({"fn": "weightPlan", "args": [25, 50, 380]})
CASES.append({"fn": "loadPlan", "args": [490, 20, 7]})
CASES.append({"fn": "loadPlan", "args": [600, 12, 9]})
CASES.append({"fn": "loadPlan", "args": [250, 30, 8]})
CASES.append({"fn": "loadPlan", "args": [800, 6, 5]})
CASES.append({"fn": "loadPlan", "args": [350, 15, 6]})
CASES.append({"fn": "loadPlan", "args": [54, 40, 4.5]})
CASES.append({"fn": "loadPlan", "args": [0, 20, 7]})
CASES.append({"fn": "loadPlan", "args": [490, 0, 7]})
CASES.append({"fn": "loadPlan", "args": [490, 20, 0]})
CASES.append({"fn": "loadPlan", "args": [8000, 2, 7]})
CASES.append({"fn": "loadPlan", "args": [700, 1, 7]})
CASES.append({"fn": "loadPlan", "args": [450, 25, 10]})
CASES.append({"fn": "costPlan", "args": [2, 0.9]})
CASES.append({"fn": "costPlan", "args": [3, 1.2]})
CASES.append({"fn": "costPlan", "args": [1, 0.75]})
CASES.append({"fn": "costPlan", "args": [4, 1.5]})
CASES.append({"fn": "costPlan", "args": [2.5, 0.8]})
CASES.append({"fn": "costPlan", "args": [7, 0.65]})
CASES.append({"fn": "costPlan", "args": [0, 0.9]})
CASES.append({"fn": "costPlan", "args": [2, 0]})
CASES.append({"fn": "costPlan", "args": [5, 2.1]})
CASES.append({"fn": "costPlan", "args": [1.5, 1.35]})
CASES.append({"fn": "costPlan", "args": [6, 0.5]})

out = []
for c in CASES:
    fn = {"weightPlan": weightPlan, "loadPlan": loadPlan, "costPlan": costPlan}[c["fn"]]
    r = fn(*c["args"])
    is_err = "error" in r
    if is_err:
        render = r["error"]
    else:
        render = {"weightPlan": renderWeight, "loadPlan": renderLoad, "costPlan": renderCost}[c["fn"]](r)
    out.append({"fn": c["fn"], "args": c["args"], "result": r, "render": render, "isError": is_err})

with open("expected.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
    f.write("\n")
print("wrote", len(out), "cases")
