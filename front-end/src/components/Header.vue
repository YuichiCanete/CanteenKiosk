<script setup>
    defineProps({
        title: String,
    })
</script>

<template>

    <div class="color-base p-3">
        <table>
            <tr>
                <td style="padding-right: 20px;">
                    <img src="../assets/Canteen Kiosk.png" alt="" style="border-radius: 100%; width: 150px;">
                </td>
                <td class="text-light" style="vertical-align: middle;">
                    <h1> Canteen Kiosk </h1>
                    <h2> {{ title }}</h2>
                </td>
            </tr>
        </table>
    </div>
    
</template>