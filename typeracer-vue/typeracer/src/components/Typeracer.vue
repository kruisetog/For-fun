<template>
  <div>
    <h3>Typeracer</h3>
    <div>
        <p>This is the quote to type out: {{ quote }}</p>
        <textarea v-model="userInput"></textarea>
    </div>
  </div>
  
</template>

<script lang="ts">
import { defineComponent, ref } from "vue"
export default defineComponent({
  name: 'Typeracer',
  components: {
    
  },
  setup(){
    const userInput = ref('')
    const quote = 'Look forward to today!'
    return{
        userInput,
        quote
    }
  }

})
</script>

<style>

</style>