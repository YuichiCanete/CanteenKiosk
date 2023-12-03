<script setup>

    import { useRouter } from 'vue-router';  
    const router = useRouter();
    const newScreen = (nscr) => {
        router.push(nscr)
    };

    import Button from 'primevue/button';
    import Image from 'primevue/image';

</script>

<template>

    <div class="pinkbg"></div>
    <div class="topbar">
        <Image src="https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/305975246_480030324173600_4611494949818294877_n.png?_nc_cat=100&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeEr57RjIzT2zI2IQkX3pZSnQWGQxV8Is6NBYZDFXwizo44xuY1kIT1yfOrKmbYzqdAxUVOp0EsS-E4HPBgFi1fY&_nc_ohc=VQCL02lBF98AX_pkHbN&_nc_ht=scontent.fcgy2-1.fna&oh=00_AfDSnbS3_4nKI7o5j51OBUpY-IkPSAc2rYhj9HN9EjrO5Q&oe=6570F5EC" alt="Image" width="150"/>
        <div>
            <Button label="Contact Us" />
            <Button label="About Us" />
        </div>
    </div>
    
    <div class="welcome">
        <p>Welcome!</p>
    </div>
    
    <div class="scanid">
        <Button label="Please Scan ID" @click="newScreen('/order')"/>
    </div>
    
    <div class="placeholder">
        <Button label="Customer" @click="newScreen('/order')"></Button>
        <Button label="Cashier" @click="newScreen('/vieworder')"></Button>
        <Button label="Finance" @click="newScreen('/finance')"></Button>
    </div>
    
</template>

<style scoped>

    .pinkbg {
        background-color: pink;
        opacity: calc(.25);
        width: 100%;
        height: 100vh;
        position: absolute;
        z-index: -1;
    }

    .welcome {
        font-size: 50px;
        font-weight: bold;
        
        background-color: white;
        width: 300px;
        
        text-align: center;
        box-shadow: 0 0 0 15px pink;

        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%,-50%);
    }

    .scanid {
        position: absolute;
        top: 65%;
        left: 50%;
        transform: translate(-50%,-50%);
    }

    .placeholder {
        position: absolute;
        top: 90%;
        left: 50%;
        transform: translate(-50%,-50%);
    }

</style>
