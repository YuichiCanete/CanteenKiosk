# How to Download and run

## Cloning

```
  git clone https://github.com/YuichiCanete/CanteenKiosk.git
```

### Front End (using vscode)

```
  cd front-end
  npm install
  npm run dev
```

### Back End (using miniconda) (edit on vscode)

```
  Open miniconda
  cd back-end
  uvicorn main:app --reload
```

### Test (using vscode)

```
  cd test-dev
  npm install cypress --save-dev
  npx cypress run
```
