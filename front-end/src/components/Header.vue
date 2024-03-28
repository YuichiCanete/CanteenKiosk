<script setup>
    defineProps({
        title: String,
    })
</script>

<template>

    <div class="color-base p-1 box-shadow">
        <table>
            <tr>
                <td style="padding-right: 20px;">
                    <img src="../assets/Canteen Kiosk.png" alt="" style="border-radius: 100%; width: 100px;" class="box-shadow m-2">
                </td>
                <td class="text-light" style="vertical-align: middle;">
                    <h1 class="text-shadow"> Canteen Kiosk </h1>
                    <h2 class="text-shadow"> {{ title }}</h2>
                </td>
            </tr>
        </table>
    </div>
    
</template>