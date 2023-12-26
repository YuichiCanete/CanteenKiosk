<script setup>
import Button from 'primevue/button'
import { ref } from 'vue'

const screen = ref('')
const header = ref('')
const orderNum = ref(0)
const currentUser = ref({})

function setScreen(newScreen, newHeader) {
  screen.value = ref(newScreen);
  header.value = ref(newHeader)
}

function checkLogin() {
  const id = document.getElementById('userId').value;
  const password = document.getElementById('userPassword').value;

  const user = users.value.find(u => u.userID == id && u.password == password);

  if (user) {
    currentUser.value = user
    if (user.userType === 'student' || user.userType === 'personnel') {
      setScreen('createOrder', 'Create Order');
    } else if (user.userType === 'cashier') {
      setScreen('viewOrder', 'View Orders');
    } else if (user.userType === 'finance') {
      setScreen('finance', 'View Orders');
    }
  } else {
    // Handle invalid login
    console.log('Invalid credentials');
    // Optionally, you can show an error message or take another action
  }
}


setScreen('login', 'Login')

const users = ref([
  {
    userID: 743,
    password: 'userpass',
    userType: 'student'
  },
  {
    userID: 744,
    password: 'userpass',
    userType: 'student'
  },
  {
    userID: 745,
    password: 'userpass',
    userType: 'personnel'
  },
  {
    userID: 746,
    password: 'userpass',
    userType: 'cashier'
  },
  {
    userID: 747,
    password: 'userpass',
    userType: 'finance'
  },
])

const foodList = ref([
  {
    Name: 'Spaghetti',
    Quantity: 0,
    Inventory: 15,
    Price: 50,
    imgUrl: 'https://urbanblisslife.com/wp-content/uploads/2023/01/Jolibee-Spaghetti-FEATURE.jpg'
  },
  {
    Name: 'Lumpia',
    Quantity: 0,
    Inventory: 50,
    Price: 5,
    imgUrl: 'https://rasamalaysia.com/wp-content/uploads/2019/03/lumpia-thumb-500x375.jpg'
  },
  {
    Name: 'Hotdog',
    Quantity: 0,
    Inventory: 25,
    Price: 15,
    imgUrl: 'https://pampangasbest.store/cdn/shop/products/Boom-boom-slim-250g-2.jpg?v=1634103216'
  },
  {
    Name: 'Egg',
    Quantity: 0,
    Inventory: 25,
    Price: 15,
    imgUrl: 'https://assets.bonappetit.com/photos/57d6ef4eabffea600db60e1a/16:9/w_2560%2Cc_limit/olive-oil-fried-egg.jpg'
  },
  {
    Name: 'Siomai',
    Quantity: 0,
    Inventory: 50,
    Price: 10,
    imgUrl: 'https://maeservesyoufood.com/wp-content/uploads/2021/12/Siomai.jpg'
  },
  {
    Name: 'Rice',
    Quantity: 0,
    Inventory: 50,
    Price: 15,
    imgUrl: 'https://hips.hearstapps.com/vidthumb/images/delish-u-rice-2-1529079587.jpg?crop=0.75xw:1xh;center,top&resize=1200:*'
  },
  {
    Name: 'Cheese Sticks',
    Quantity: 0,
    Inventory: 45,
    Price: 15,
    imgUrl: 'https://www.ladyschoice.com.ph/content/dam/brands/lady_s_choice/philippines/106602187-cheese-sticks.png'
  },
  {
    Name: 'Pizza',
    Quantity: 0,
    Inventory: 10,
    Price: 45,
    imgUrl: 'https://www.seriouseats.com/thmb/-_mziT2tl0F63I4kfji4S6bE-cA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2018__10__20181015-state-of-slice-delmar-clay-williams-2de043fa5a0d4475b6c567e4a974b13b.jpg'
  },
  {
    Name: 'Magnolia',
    Quantity: 0,
    Inventory: 50,
    Price: 15,
    imgUrl: 'https://shopustore.net/cdn/shop/products/8434b17f0fa14d98dc749d38c03b171e_grande.jpg?v=1634361815'
  },
  {
    Name: 'Mentos',
    Quantity: 0,
    Inventory: 30,
    Price: 5,
    imgUrl: 'https://www.candywarehouse.com/cdn/shop/files/mini-mentos-rainbow-candy-rolls-100-piece-tub-candy-warehouse-1.jpg?v=1689319664'
  },
])

const orderList = ref([])

function getTotal() {
  let total = 0;
  for (const item of foodList.value) {
    total += item.Price * item.Quantity;
  }
  return total;
}

function incrementQuantity(idx) {
  foodList.value[idx].Quantity = Math.min(foodList.value[idx].Quantity + 1, foodList.value[idx].Inventory)
}

function decrementQuantity(idx) {
  foodList.value[idx].Quantity = Math.max(foodList.value[idx].Quantity - 1, 0)

}

function incrementInventory(idx) {
  foodList.value[idx].Inventory += 1
}

function decrementInventory(idx) {
  foodList.value[idx].Inventory = Math.max(foodList.value[idx].Inventory - 1, 0)
}

function addOrder(paytype) {
  const userCash = document.getElementById('userCash').value;
  if (paytype === 'tally' || (paytype === 'cash' && parseFloat(userCash) >= getTotal())) {
    const proceed = confirm('Do you want to proceed with this order?');
    if (proceed) {
      orderNum.value += 1;
      let currentOrder = ref([]);

      // Create a copy of foodList with quantities reset to 0
      let foodListCopy = JSON.parse(JSON.stringify(foodList.value));
      let itemsToAddToOrder = [];

      for (let item of foodListCopy) {
        if (item.Quantity > 0) {
          item.Inventory -= item.Quantity
          // Create a deep copy of the item to maintain original quantities
          let newItem = { ...item };
          itemsToAddToOrder.push(newItem);
          // Reset quantity in foodList to 0
          item.Quantity = 0;
        }
      }

      currentOrder.value = itemsToAddToOrder;
      const currentDate = new Date();
      const day = currentDate.getDate().toString().padStart(2, '0');
      const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // Month is zero-indexed
      const year = currentDate.getFullYear();
      const formattedDate = `${day}/${month}/${year}`;

      orderList.value.push({
        User: currentUser.value,
        Menu: JSON.parse(JSON.stringify(currentOrder.value)), // Create a deep copy of currentOrder.value
        Total: getTotal(),
        Paytype: paytype,
        Ordernum: orderNum.value,
        Cash: userCash,
        CashBack: userCash - getTotal(),
        Date: formattedDate,
      });

      setScreen('orderSuccess', 'Order Success');

      foodList.value = foodListCopy; // Update foodList with quantities reset to 0
    } else {
      alert('Order has been Cancelled')
    }

  } else {
    // Provide a message to the user that their cash input is insufficient
    alert('Insufficient cash for the order');
  }
}

function newItem() {
  const imgUrl = document.getElementById('insertUrl').value;
  const Name = document.getElementById('insertName').value;
  const Price = parseInt(document.getElementById('insertPrice').value);
  const Inventory = parseInt(document.getElementById('insertInventory').value);

  if (imgUrl && Name && !isNaN(Price) && !isNaN(Inventory)) {
    foodList.value.push({
      Name: Name,
      Quantity: 0,
      Inventory: Inventory,
      Price: Price,
      imgUrl: imgUrl
    });

    clearForm();
    console.log('New item added:', foodList); // Log the updated foodList
  } else {
    alert('Please fill in all fields with valid values');
  }
}

function clearForm() {
  document.getElementById('insertUrl').value = '';
  document.getElementById('insertName').value = '';
  document.getElementById('insertPrice').value = '';
  document.getElementById('insertInventory').value = '';
}

function removeOrder(idx) {
  orderList.value.splice(idx, 1);
}

function removeFood(idx) {
  foodList.value.splice(idx, 1);
}


</script>

<template>
  <div v-if="screen.value == 'login'" class="imgBackground"></div>

  <!-- Topbar -->
  <div class="topBar flexRow pinkBackground">
    <h1>{{ header.value }}</h1>
    <img src="./assets/Canteen Kiosk.png" alt="App Logo" class="logo border shadow">
  </div>

  <!-- login screen -->
  <div v-if="screen.value == 'login'">

    <!-- login box -->


    <div class="loginBox pinkBackground roundBorder flexColumn shadow">

      <h1>Canteen Kiosk</h1>
      <h3>Scan Id</h3>
      <p>or</p>
      <h3>Login Manually</h3>
      <input type="text" placeholder="User ID" class="roundBorder inputText shadow" id="userId">
      <input type="password" placeholder="Password" class="roundBorder inputText shadow" id="userPassword">
      <input type="button" value="Login" class="button roundBorder shadow" @click="checkLogin()">
    </div>

  </div>

  <!-- Create Order -->
  <div v-else-if="screen.value == 'createOrder'">
    <div class="createOrderContainer flexRow">

      <!-- Create Order: left -->
      <div class="orderBox pinkBackground roundBorder border shadow">
        <h2>Menu</h2>

        <div class="wrapping scrolling" style="width: 100%; height: 95%;">

          <!-- Order Items -->
          <div v-for="(item, index) in foodList" :key="index">
            <!-- TODO: add image here -->
            <div v-if="item.Inventory > 0" class="orderFood roundBorder shadow">
              <div style="text-align: center;">
                <img style="width: 150px; height: 125px; margin: 10px auto;" class="roundBorder" :src="item.imgUrl"
                  :alt="item.Name">
              </div>
              <p>{{ item.Name }} </p>
              <p style="margin-bottom: 10px;">P{{ item.Price }}</p>
              <div class="flexRow" style="justify-content: space-between; width: 100%; place-items: center;">
                <button class="button roundBorder plusMinus shadow" @click="decrementQuantity(index)"> - </button>
                <h2 style="font-size: 15px;">{{ item.Quantity }}/{{ item.Inventory }}</h2>
                <button class="button roundBorder plusMinus shadow" @click="incrementQuantity(index)"> + </button>
              </div>
            </div>
          </div>

        </div>

      </div>

      <!-- Create Order: right -->
      <div class="selectedOrderBox pinkBackground roundBorder border shadow">
        <h2>Selected Items</h2>

        <!-- Selected Items -->
        <div class="scrolling" style="width: 100%; height: 60%;">
          <div v-for="(item, index) in foodList" :key="index">
            <div v-if="item.Quantity > 0" class="selectedFood roundBorder shadow">
              <p>{{ item.Name }} x{{ item.Quantity }}</p>
              <p>P{{ item.Price * item.Quantity }}</p>
            </div>
          </div>
        </div>

        <!-- Total Amount -->
        <div class="total flexColumn">
          <h3 style="margin-bottom: 15px;">Total Price: P{{ getTotal() }}</h3>
          <p>Order Confirmation:</p>
          <p>Select Payment Type</p>
          <div class="flexRow">
            <input type="number" placeholder="Input Cash" class="roundBorder shadow border inputText" id="userCash"
              style="width: 50%;">
            <input type="button" value="Cash" class="button roundBorder shadow" @click="addOrder('cash');">
            <div v-if="currentUser.userType == 'personnel'">
              <input type="button" value="Tally" class="button roundBorder shadow" @click="addOrder('tally')">
            </div>
            <div v-else-if="currentUser.userType != 'personnel'">
              <input type="button" value="Tally" class="button roundBorder shadow" style="opacity: calc(75%);">
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>

  <div v-else-if="screen.value == 'orderConfirm'">
    <!-- Code this if have enough time -->
  </div>

  <!-- Order Success -->
  <div v-else-if="screen.value == 'orderSuccess'">

    <!-- Order Success box -->
    <div class="orderSuccessBox pinkBackground roundBorder">
      <h1>Order Success</h1>
      <p>Your waiting number is...</p>
      <h1>{{ orderNum }}</h1>
      <input type="button" value="New Order" class="button roundBorder shadow"
        @click="setScreen('createOrder', 'Create Order')">
      <input type="button" value="Log Out" class="button roundBorder shadow" @click="setScreen('login', 'Login')">
    </div>

  </div>

  <!-- View Order -->
  <div v-else-if="screen.value == 'viewOrder'">

    <div class="viewOrderTable pinkBackground roundBorder shadow">
      <div style="height: 90%; overflow-y: scroll;">
        <table style="justify-content: space-between; width: 100%;">

          <tr>
            <th>User</th>
            <th>Order</th>
            <th>Pay Type</th>
            <th>Total</th>
            <th>Cash</th>
            <th>Change</th>
            <th>Date</th>
            <th>Process Order</th>
          </tr>

          <tr v-for="(order, index) in orderList" :key="index" style="background-color: white;">

            <td style="vertical-align: top;">
              <p>{{ order.User.userID }}</p>
            </td>

            <td style="vertical-align: top;">
              <div v-for="(item, index2) in order.Menu" :key="index2">
                <p>{{ item.Name }} x{{ item.Quantity }}</p>
              </div>
            </td>

            <td style="vertical-align: top;">
              {{ order.Paytype }}
            </td>

            <td style="vertical-align: top;">
              P{{ order.Total }}
            </td>

            <td style="vertical-align: top;">
              <p v-if="order.Paytype != 'tally'">P{{ order.Cash }}</p>
            </td>

            <td style="vertical-align: top;">
              <p v-if="order.Paytype != 'tally'">P{{ order.CashBack }}</p>
            </td>

            <td style="vertical-align: top;">
              {{ order.Date }}
            </td>

            <td style="vertical-align: top;">
              <button class="roundBorder button pinkBackground" @click="removeOrder(index)">Confirm</button>
              <button class="roundBorder button pinkBackground" @click="removeOrder(index)">Cancel</button>
            </td>

          </tr>

        </table>
      </div>
      <input type="button" value="Edit Menu" class="button roundBorder shadow"
        @click="setScreen('editMenu', 'Edit Menu')">
    </div>

  </div>

  <!-- Edit Menu -->
  <div v-else-if="screen.value == 'editMenu'">


    <div class="createOrderContainer flexRow">

      <!-- Edit Menu: left -->
      <div class="orderBox pinkBackground roundBorder border shadow">
        <h2>Edit Menu (Inventory)</h2>

        <div class="wrapping scrolling" style="width: 100%; height: 95%;">
          <div v-for="(item, index) in foodList" :key="index" class="orderFood roundBorder shadow" style="height: 330px;">
            <!-- Food Image Here -->
            <img style="width: 125px; height: 125px; margin: 10px auto;" class="roundBorder" :src="item.imgUrl"
              :alt="item.Name">
            <p>{{ item.Name }} </p>
            <p style="margin-bottom: 10px;">P{{ item.Price }}</p>
            <div class="flexRow" style="justify-content: space-between; width: 100%; place-items: center;">
              <button class="button roundBorder plusMinus shadow" @click="decrementInventory(index)"> - </button>
              <h2>{{ item.Inventory }}</h2>
              <button class="button roundBorder plusMinus shadow" @click="incrementInventory(index)"> + </button>
            </div>
            <div style="text-align: center;">
              <button class="button roundBorder plusMinus shadow"
                style="width: 125px; font-size: 15px; margin: 15px auto;" @click="removeFood(index)">Remove Item</button>
            </div>
          </div>
        </div>

      </div>

      <!-- Edit Menu Right -->
      <div class="addItemBox pinkBackground roundBorder border shadow">
        <h2>Add Item</h2>

        <div class="flexColumn">
          <img v-if="imageUrl" :src="imageUrl" class="newItemImg roundBorder shadow" alt="Food Image">
          <input type="text" placeholder="Insert image Url" class="inputText roundBorder shadow" id="insertUrl"
            v-model="imageUrl">
          <input type="text" placeholder="Insert Food Name" class="inputText roundBorder shadow" id="insertName">
          <input type="number" placeholder="Insert Food Price" class="inputText roundBorder shadow" id="insertPrice">
          <input type="number" placeholder="Insert Food Inventory" class="inputText roundBorder shadow"
            id="insertInventory">
          <button class="button roundBorder shadow border" @click="newItem">Add Item</button>
        </div>






      </div>



    </div>

  </div>

  <!-- View Orders: Finance -->
  <div v-else-if="screen.value == 'finance'">
    <div class="viewOrderTable pinkBackground roundBorder shadow" style="overflow-y: scroll;">

      <table style="justify-content: space-between; width: 100%;">

        <tr>
          <th>User</th>
          <th>Order</th>
          <th>Pay Type</th>
          <th>Total</th>
          <th>Cash</th>
          <th>Change</th>
          <th>Date</th>
        </tr>

        <tr v-for="(order, index) in orderList" :key="index" style="background-color: white;">

          <td style="vertical-align: top;">
            <p>{{ order.User.userID }}</p>
          </td>

          <td style="vertical-align: top;">
            <div v-for="(item, index2) in order.Menu" :key="index2">
              <p>{{ item.Name }} x{{ item.Quantity }}</p>
            </div>
          </td>

          <td style="vertical-align: top;">
            {{ order.Paytype }}
          </td>

          <td style="vertical-align: top;">
            P{{ order.Total }}
          </td>

          <td style="vertical-align: top;">
            <p v-if="order.Paytype != 'tally'">P{{ order.Cash }}</p>
          </td>

          <td style="vertical-align: top;">
            <p v-if="order.Paytype != 'tally'">P{{ order.CashBack }}</p>
          </td>

          <td style="vertical-align: top;">
            {{ order.Date }}
          </td>

        </tr>

      </table>

    </div>

  </div>

  <div class="logout" v-if="screen.value != 'login'">
    <button class="button roundBorder border shadow" @click="setScreen('login', 'Login')">Logout</button>
  </div>
</template>


<script>
export default {
  data() {
    return {
      imageUrl: '' // Initialize imageUrl as an empty string
      // Other data properties for food details
    };
  },
  methods: {
    newItem() {
      // Logic to add a new food item
    }
  }
};
</script>



<style scoped>
/* Behaviours */

.th {
  padding: 50px;
}

.flexRow {
  display: flex;
  flex-direction: row;
}

.flexColumn {
  display: flex;
  flex-direction: column;
}

.pinkBackground {
  background-color: pink;
}

.roundBorder {
  border-radius: 15px;
}

.border {
  border: 3px solid rgb(233, 128, 146);
}

.shadow {
  box-shadow: 4px 4px 0 0 rgb(233, 128, 146);
}

.scrolling {
  overflow-y: auto;
}

.inputText {
  border: 2px solid rgb(233, 128, 146);
  outline: none;
  margin: 5px;
  padding: 10px;
  transition: .5s;
}

.inputText:focus {
  border: 2px solid rgb(163, 33, 55);
}

.inputText:active {
  scale: 90%;
}

.button {
  outline: none;
  border: none;
  margin: 5px;
  padding: 10px;
  transition: .25s;
}

.button:active {
  scale: 90%;
}

.wrapping {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

/* Components */
.topBar {
  padding: 15px;
  justify-content: space-between;
  place-items: center;
}

.logo {
  width: 100px;
  height: 100px;
  border-radius: 100px;
}

.loginBox {
  width: min(55%, 350px);
  text-align: center;
  padding: 15px;
  margin: 20vh auto;
  text-align: center;
  align-items: center;
}

.createOrderContainer {
  margin: 5vh auto;
  width: 90%;
  height: 70vh;
}

.orderBox {
  width: 65%;
  margin-right: 5%;

  padding: 15px;
}

.selectedOrderBox {
  width: 30%;
  padding: 15px;
}

.orderFood {
  padding: 15px;
  margin: 15px;
  width: 175px;
  height: 275px;
  background-color: white;
}

.selectedFood {
  margin: 10px 0;
  padding: 10px;
  background-color: white;
  width: 95%;
  display: flex;
  justify-content: space-between;

}

.total {
  margin: 5%;
  text-align: center;
  align-items: center;
}

.orderSuccessBox {
  width: min(55%, 350px);
  text-align: center;
  padding: 15px;
  margin: 20vh auto;
  text-align: center;
  align-items: center;
}

.plusMinus {
  font-size: 20px;
  padding: 5px;
  margin: 0;
  width: 40px;
  height: 40px;
}

.viewOrderTable {
  width: 60%;
  height: 70vh;
  padding: 15px;
  margin: 5vh auto;
}

.newItemImg {
  width: 175px;
  height: 175px;
  margin: 10px auto;
  background-color: red;
}

.addItemBox {
  width: 30%;
  text-align: center;
  padding: 15px;
}

.imgBackground {
  position: absolute;
  z-index: -1;
  background-image: url('https://scontent.fdvo1-1.fna.fbcdn.net/v/t1.6435-9/121265108_2837965773097979_3060103412268296208_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=7f8c78&_nc_eui2=AeHQMtvaAKjyDL5nzyfKze0es8Z0ImYFU6uzxnQiZgVTq1eKm4tXuEfQ5asCAQ6N1PXRD1MTZ1KMMbOGTMQPWVVv&_nc_ohc=d8a5yQpjZM0AX-pHOZh&_nc_ht=scontent.fdvo1-1.fna&oh=00_AfD27UzEMpmYi5815dlYJmde_4RaYCs5oPYrBW4lXgXx3w&oe=65B08747');
  width: 100%;
  height: 100vh;
  background-size: cover;
  background-position: center;
}

.logout {
  position: absolute;
  top: 93%;
  left: 1%;
}
</style>
