import data from "./data.json";

const realData = data.data;

// function to determine age bucket
const determineAgeGroup = (age) => {
  if (age < 10) return "<10";
  if (age >= 80) return "≥80";
  if (isNaN(age) || typeof age !== "number") return;

  const lowerBound = Math.floor(age / 10) * 10;
  const upperBound = lowerBound + 9;

  return `${lowerBound}-${upperBound}`;
};

// creates an object (python dictionary), that contains all the age data for one location and the total amount of people

const cleanJsonData = () => {
  const cleanedData = {};
  for (let i = 0; i < realData.length; i++) {
    let currentItem = realData[i];
    let { name, age } = currentItem;
    if (!cleanedData[name]) {
      cleanedData[name] = {
        "<10": 0,
        "10-19": 0,
        "20-29": 0,
        "30-39": 0,
        "40-49": 0,
        "50-59": 0,
        "60-69": 0,
        "70-79": 0,
        "≥80": 0,
        total: 0,
      }
    }
    let ageRange = determineAgeGroup(age);
    cleanedData[name][ageRange] += 1;
    cleanedData[name]["total"] += 1;
  }
  return cleanedData;
};

export const createPercentObjs = (name, placeObj) => {
  const ageObjs = [];
  const { total } = placeObj;
  for (const [key, value] of Object.entries(placeObj)) {
    if (key !== "total") {
      const newAgeObj = { name: name, age: key, population: value / total };
      ageObjs.push(newAgeObj);
    }
  }
  return ageObjs;
};

//function to create and return array with objects that contain name, age, and sample size as keys

export const calcPercentages = (cleanedData) => {
  let percentsArr = [];
  const locationNames = Object.keys(cleanedData);
  for (let i = 0; i < locationNames.length; i++) {
    let currentName = locationNames[i];
    let currentItem = cleanedData[currentName];
    let newPercentObjsArr = createPercentObjs(currentName, currentItem);
    for (let j = 0; j < newPercentObjsArr.length; j++) {
      let currentPercentObj = newPercentObjsArr[j];
      percentsArr.push(currentPercentObj);
    }
  }
  return percentsArr;
};

export const testClean = cleanJsonData();

export const calculatedPercents = calcPercentages(testClean);
