<script setup>
import { ref } from 'vue';
import AppMenuItem from './AppMenuItem.vue';
const model = ref([
    {
        label: 'Home',
        items: [{ label: 'Dashboard', icon: 'pi pi-fw pi-home', to: '/' }]
    },
    {
        label: 'Recrutamento e Selecção',
        items: [
            { label: 'Painel', icon: 'pi pi-fw pi-home', to: '/recutamento/painel' },
            { label: 'Candidato', icon: 'pi pi-fw pi-user', to: '/recutamento/candidato' },
            { label: 'Campanha', icon: 'pi pi-fw pi-users', to: '/recutamento/campanha' },
            { label: 'Programar Entrevista', icon: 'pi pi-fw pi-bookmark', to: '/recutamento/programarEntrevista' },
            { label: 'Canais de Recrutamento', icon: 'pi pi-fw pi-address-book', to: '' },
            { label: 'Portais de Recrutamento', icon: 'pi pi-fw pi-address-book', to: '' },
            
            
            
        ]
    },
    
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
        
    </ul>
</template>

<style lang="scss" scoped></style>
