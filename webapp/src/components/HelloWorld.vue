<script setup lang="ts">
import { ref, inject } from 'vue'

const props = defineProps<{ isAuthenticated: boolean, count?: number }>()
const csrfToken = inject<string>('csrfToken')
const count = ref(props.count || 0)

async function increment() {
  if (!csrfToken) return;
  try {
    const response = await fetch('/api/me/count', {
      credentials: 'same-origin',
      mode: 'same-origin',
      method: 'PATCH',
      headers: {
        'X-CSRFToken': csrfToken
      },
    })
    if (response.ok) {
      const data: { updatedCount: number } = await response.json()
      count.value = data.updatedCount
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
    <button class="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2" type="button" @click="increment" :disabled="!isAuthenticated">count is {{ count }}</button>
</template>
