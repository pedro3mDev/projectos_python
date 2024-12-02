<script setup>
    import { useLayout } from '@/layout/composables/layout';
    import { computed } from 'vue';
    const { layoutConfig } = useLayout();
    const logoUrl = computed(() => {
        return `/layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
    });
</script>

<template>
    <div class="layout-footer">
        <img :src="logoUrl" alt="Logo" height="60" class="mr-2" />
        Copyrigth 2025 All Rigth Reserved
    </div>
</template>
<style lang="scss" scoped></style>

