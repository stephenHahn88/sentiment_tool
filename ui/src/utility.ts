import {router} from '@/main'
import {round} from "lodash";


export async function pushRouter(path: string) {
    await router.push({path: path})
}

export function timeString(seconds: number) {
    let minutes = Math.floor(seconds / 60).toString()
    let leftoverSeconds = round(seconds % 60)
    let extra = ""
    if (leftoverSeconds < 10) {
        extra = "0"
    }
    return `${minutes}:${extra}${leftoverSeconds.toString()}`
}

export function createLabels(duration: number, numLabels: number) {
  let labels = [];
  for (let i = 0; i <= round(duration); i += round(duration) / numLabels) {
    labels.push(timeString(i));
  }
  return labels;
}

// Code taken from: https://dev.to/trekhleb/weighted-random-algorithm-in-javascript-1pdc
export function weightedRandom(items: string[], weights: number[]) {

  if (items.length !== weights.length) {
    throw new Error('Items and weights must be of the same size');
  }

  if (!items.length) {
    throw new Error('Items must not be empty');
  }

  const cumulativeWeights: number[] = [];
  for (let i = 0; i < weights.length; i += 1) {
    cumulativeWeights[i] = weights[i] + (cumulativeWeights[i - 1] || 0);
  }

  // Getting the random number in a range of [0...sum(weights)]
  // For example:
  // - weights = [1, 4, 3]
  // - maxCumulativeWeight = 8
  // - range for the random number is [0...8]
  const maxCumulativeWeight = cumulativeWeights[cumulativeWeights.length - 1];
  const randomNumber = maxCumulativeWeight * Math.random();

  // Picking the random item based on its weight.
  // The items with higher weight will be picked more often.
  for (let itemIndex = 0; itemIndex < items.length; itemIndex += 1) {
    if (cumulativeWeights[itemIndex] >= randomNumber) {
      return items[itemIndex];
    }
  }

}