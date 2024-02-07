<script setup>
    const props =  defineProps({
        avatarImage:{type: String},
        name:{type: String},
        message:{type: String},
        side:{type: String}
    })


    const cardStyle = computed(() => {
    
    switch(props.side){
        case 'left':
            return {
                color:'#B1E5F2',size:'15px'
            }
        case 'right':
        return {
                color:'#FAFFD8',size:'15px'
            }
        default:
        return {
                color:'#D7FDF0',size:'15px'
            }
    }
});
    
</script>

<template>
    <div class="question">
        <Fieldset :class="props.side == 'left' ? 'answer' : 'question'">
                <template #legend>
                    <div class="flex align-items-center pl-2">
                        <Avatar :image="props.avatarImage" shape="circle" />
                        <span class="font-bold">{{props.name}}</span>
                    </div>
                </template><br>
                <p class="m-0">
                    {{ props.message }}
                </p>
        </Fieldset>
    </div>
</template>


<style scoped lang="scss">
/* .p-fieldset-legend > div{
    background-color: v-bind(cardStyle.color);
    border-radius: 25px;
    justify-content: center;
    align-items: center;
    display: flex;
    font-size: v-bind(cardStyle.size);
} */

.answer .p-fieldset-legend > div{
    background-color: v-bind(cardStyle.color);
    border-radius: 25px;
    justify-content: center;
    align-items: center;
    display: flex;
    font-size: v-bind(cardStyle.size);
} 

.question{
    .p-fieldset-legend > div{
    background-color: v-bind(cardStyle.color);
    border-radius: 25px;
    justify-content: center;
    align-items: center;
    display: flex;
    font-size: v-bind(cardStyle.size);
    }

    .p-toggleable-content .p-fieldset-content p  {
        background-color: red;
        color: #000;
    }

} 

</style>