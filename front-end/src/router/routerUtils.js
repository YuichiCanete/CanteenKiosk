import { useRouter } from "vue-router";
function switchTo(path) {
    const router = useRouter()
    router.push(path);
}