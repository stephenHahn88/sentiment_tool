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