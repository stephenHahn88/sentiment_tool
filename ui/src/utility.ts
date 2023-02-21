import {router} from '@/main'


export async function pushRouter(path: string) {
    await router.push({path: path})
}
