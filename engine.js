/* Towel math engine - pure arithmetic, every borrowed number labeled. */
(function (root) {
  "use strict";
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }

  function weightPlan(widthCm, heightCm, gsm) {
    if (!(widthCm > 0) || !(heightCm > 0) || !(gsm > 0)) return { error: "size and GSM must be positive" };
    var grams = r1(widthCm * heightCm / 10000 * gsm);
    return { widthCm: widthCm, heightCm: heightCm, gsm: gsm, grams: grams };
  }

  function loadPlan(towelG, count, machineKg) {
    if (!(towelG > 0) || !(count > 0) || !(machineKg > 0)) return { error: "weight, count and capacity must be positive" };
    var perLoad = Math.floor(machineKg * 1000 / towelG);
    if (perLoad < 1) return { error: "one towel is heavier than the machine's labeled capacity" };
    var loads = Math.ceil(count / perLoad);
    return { towelG: towelG, count: count, machineKg: machineKg, perLoad: perLoad, loads: loads };
  }

  function costPlan(loadsWeek, costPerLoad) {
    if (!(loadsWeek > 0) || !(costPerLoad > 0)) return { error: "loads and cost must be positive" };
    var loadsYear = Math.round(loadsWeek * 52);
    var costYear = r2(loadsYear * costPerLoad);
    return { loadsWeek: loadsWeek, costPerLoad: costPerLoad, loadsYear: loadsYear, costYear: costYear };
  }

  function renderWeight(r) {
    return "A " + r.widthCm + " x " + r.heightCm + " cm towel at a labeled " + r.gsm + " GSM weighs " + r.grams + " g.";
  }

  function renderLoad(r) {
    return "At " + r.towelG + " g a towel, a labeled " + r.machineKg + " kg machine takes " + r.perLoad + " towels a load - " + r.count + " towel" + (r.count === 1 ? "" : "s") + " is " + r.loads + " load" + (r.loads === 1 ? "" : "s") + ".";
  }

  function renderCost(r) {
    return r.loadsWeek + " loads a week at a labeled " + r.costPerLoad + " a load is " + r.loadsYear + " loads and about " + r.costYear + " a year.";
  }

  var api = { weightPlan: weightPlan, loadPlan: loadPlan, costPlan: costPlan,
              renderWeight: renderWeight, renderLoad: renderLoad, renderCost: renderCost };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.TowelMath = api;
})(typeof window !== "undefined" ? window : this);
