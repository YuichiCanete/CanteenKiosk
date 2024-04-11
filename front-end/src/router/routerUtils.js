import { useRouter } from "vue-router";

export const switchTo = (path) => {
    const router = useRouter()
    router.push(path);
}
