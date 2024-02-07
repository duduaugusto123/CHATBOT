<script setup>
    let message = ref("")
    let response = ref("")
    
    const sendMessage = async () => {
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: message
            }
        })
        response.value = answer.value
       
    }
    const dialog = {
        type: '',
        message: ''        
    }
    let dialogs = ref([])

    const addDialog = computed((diag) => dialogs.push(diag))
</script>

<template>
    <div class="conteiner">
        <div v-for="(d, index) in dialogs" :key="index">
            <TextBox avatarImage="dominic.jpeg" name="Toretto" message="d.message" side="d.type"></TextBox>
        </div>
        <div class="response_chat">
            
            <br>
            <TextBox avatarImage="patolino.jpeg" name="Patolino O Mago" message="Contemplem o Magooooooo" side="red"></TextBox>
        </div>
            <div class="question">
                <label for=""> Type here your message!</label> <br>
                <textarea id="input_question" v-model="message"/> <br> <br>
                <Button @click="sendMessage">Send</Button>
                <br>
            </div>
        <br>
          
    </div>
</template>

<style scoped >
     
    .conteiner{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .response_chat{
        display: flex;
        flex-direction: column;
        width: 60rem;
    }
    
    #input_question{
        display: flex;
        border-radius: 15px;
        border: 1px solid rgb(56, 56, 56);
        justify-content: center;
        align-items: center;
    }
</style>