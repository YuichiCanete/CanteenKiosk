




const startData = {

    orderNum:69,
    incrementOrder: function(){
        this.orderNum += 1
    },

    foodList: [],
    addFood: function(name,quantity,price){
        this.foodList.push({
            name:name,
            quantity:quantity,
            price:price
        })
    }

}

startData.addFood('Egg',20,20)
startData.addFood('Hotdog',10,10)

export const data = startData

