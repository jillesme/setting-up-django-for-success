<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{ isAuthenticated: boolean, count?: number }>()
const count = ref(props.count || 0)
</script>

<template>
    <button type="button" @click="count++" :disabled="!isAuthenticated">count is {{ count }}</button>
</template>
