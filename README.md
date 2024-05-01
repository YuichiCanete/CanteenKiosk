# How to Download and run

## Cloning

```
  git clone https://github.com/YuichiCanete/CanteenKiosk.git
```

## Front End (using vscode)

### Setup
```
  cd front-end
  npm install primevue
  npm install primeicons
```

### To Run
```
  cd front-end
  npm run dev
```

## Back End (using miniconda)

Create new db named canteen_kiosk then
Import the canteen_kiosk.sql to phpmyadmin

### Setup
```
  cd back-end
  conda create --name canteen_kiosk python=3.9
  conda activate canteen_kiosk
  pip install fastapi uvicorn mysql-connector-python python-multipart cryptography bcrypt
```

### To Run
```
  cd back-end
  conda activate canteen_kiosk
  uvicorn main:app --reload
```

## Test (using vscode)

```
  cd test-dev
  npm install cypress --save-dev
  npx cypress run
```
