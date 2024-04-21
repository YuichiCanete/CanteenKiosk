import {ref} from 'vue'
import axios from 'axios';

class StartData {
    constructor() {
        this.myUrl = ''
        this.orderNum = 0;
        this.payType = 'cash'
        this.foodList = [];
        this.orderList = [];
        this.userList = [];
        this.currentUser = {}
    }

    loginUser(user){
        this.currentUser = user;
        console.log("Welcome: "+user.userID)
    }

    addUser(userID,password,userType){
        this.userList.push({
            userID:userID,
            password:password,
            userType:userType
        })
    }

    incrementOrder() {
        this.orderNum += 1;
    }

    addFood(name, inventory, price) {
        this.foodList.push({
            name: name,
            inventory: inventory,
            price: price,
            quantity: 0
        });
    }

    addOrder() {
        this.orderNum += 1;
        const newFoodList = [...this.foodList];
        const newPayType = this.payType;
        const userOrder = {
            orderNum: this.orderNum,
            foodList: newFoodList,
            payType: newPayType,
            date: '0000-00-00'
        };
        this.orderList.push({...userOrder}); 
        console.log(userOrder)
        this.resetOrder();
        console.log(userOrder)
    }
    
    
    resetOrder() {
        const newFoodList = this.foodList.map(food => ({ ...food }));
        newFoodList.forEach(function (food) {
            food.quantity = 0;
        });
        this.foodList = newFoodList;
    }
    
    addFoodToOrder(name){
        this.foodList.forEach(function(food){
            if (food.name === name){
                food.quantity += 1
            }
        })
    }

    incrementFood(name){
        this.foodList.forEach(function(food){
            if (food.name === name & food.quantity < food.inventory){
                food.quantity += 1
            }
        })
    }

    decrementFood(name){
        this.foodList.forEach(function(food){
            if (food.name === name & food.quantity > 0){
                food.quantity -= 1
                console.log(food)
            }
        })
    }

    getTotal(fl){
        let total = 0
        fl.forEach(function(food){
            total += food.quantity * food.price
        })
        return total
    }
}

class meOrder{
    constructor(){
        this.foodList = []
    }

    addFood(food,price,available_stock){
        let existingFood = this.foodList.find(f => f.food_name === food);
        if (existingFood) {
            console.log("Food already exists in the list.");
        } else {
            this.foodList.push({
                food_name: food,
                price: price,
                available_stock: available_stock,
                quantity: 1,
            });
        }
    }

    incFood(food){
        this.foodList.forEach(function(f){
            if (f.food_name===food && f.quantity < f.available_stock){
                f.quantity += 1
            }
        })
    }

    decFood(food) {
        this.foodList.forEach((f, index) => {
            if (f.food_name === food && f.quantity > 0) {
                f.quantity -= 1;
                if (f.quantity === 0) {
                    this.foodList.splice(index, 1); // Remove the element from the array
                }
            }
        });
    }
}

class apiFunctions {

    async get(linkRoute) {
        try {
            const response = await axios.get(linkRoute);
            console.log('Get Success');
            console.log(response.data)
            return {
                isSuccess: true,
                data: response.data
            }
        } catch (error) {
            console.error('Error Message:', error);
            return {
                isSuccess: false,
                data: []
            };
        }
    }

    async update(linkRoute,updatedObject){
        try {
          const response = await axios.put(linkRoute, updatedObject,{
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
        });
          console.log('Update Success');
        } catch (err) {
          console.error('Update Error:', err);
        }
    }

    async add(linkRoute,addObject){
        try {
            await axios.post(linkRoute, addObject, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                }
            });
            console.log('Adding Success')
        } catch (err) {
            console.error('Adding Error:', err);    
        }
    }

    async remove(linkRoute){
        // Make sure naay ID
        try {
            await axios.delete(linkRoute);   
            console.log('Delete Success')
        } catch (err) {
            console.error('Deleting Error:', err);
        }
    }
}

// [Extract Id from link]
// const router = useRouter();
// const expenseId = parseInt(router.currentRoute.value.params.expenseId);

// Example usage:
const data = ref(new StartData())
const apiFunc = ref(new apiFunctions())
const myOrder = ref(new meOrder())
export { data , apiFunc, myOrder};
