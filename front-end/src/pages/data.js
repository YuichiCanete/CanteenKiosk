import {ref} from 'vue'
import axios from 'axios';

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
const apiFunc = ref(new apiFunctions())
const myOrder = ref(new meOrder())
export { apiFunc, myOrder};
