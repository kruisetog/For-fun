<template>
  <div>
    <h3>Typeracer</h3>
    <div>
        <p>This is the quote to type out: </p>
        <div>
          <span v-for="a_word,index of wordList" :key="index">
            <span v-if="index == wordIndex" style="text-decoration: underline">
              <span v-for="a_letter, a_letterIndex of a_word" :key="a_letterIndex">
                <span v-if="a_letterIndex <= letterIndex" style="background-color: grey;">
                  {{ a_letter }}
                </span>
                <!-- <span v-if="letterIndex == wrongLetterIndex" style="background-color: red;">
                  {{ a_letter }}
                </span> -->
                <span v-else>
                  {{ a_letter }}
                </span>
              </span>
            </span>
            <span v-else >
              {{ a_word }}
            </span> 
            <!-- {{ ' ' }} -->
          </span>
        </div>
        

        <textarea v-model="userInput"></textarea>
    </div>
  </div>
  
</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from "vue"
export default defineComponent({
  name: 'Typeracer',
  components: {
    
  },
  setup(){
    const userInput = ref('')
    const quote = 'Look forward to today!'
    const wordIndex = ref(0)
    const letterIndex = ref(0)
    let wrongLetterIndex = 0
    const wordList = computed(()=>{
      const result = []
      for(let a_word of quote.split(' ')){
        result.push(a_word)
        result.push(' ')
      }
      result.pop()
      return result
    })
    watch(userInput, () =>{
      if(userInput.value == wordList.value[wordIndex.value]){
        userInput.value = ''
        wordIndex.value++
      }
      if(wordList.value[wordIndex.value].search(userInput.value) != -1){
        wrongLetterIndex = -1 //when letter is not wrong
        letterIndex.value = userInput.value.length - 1
      }
      else{
        wrongLetterIndex = userInput.value.length - 1
      }
      
    })
  

    return{
      userInput,
      quote,
      wordList,
      wordIndex,
      letterIndex,
      wrongLetterIndex
    }
  }

})
</script>

<style>

</style>