import { useRouter } from "vue-router";

export const pageChange = () => {
    const switchTo = (path) => {
        const router = useRouter()
        router.push(path);
    }
}
