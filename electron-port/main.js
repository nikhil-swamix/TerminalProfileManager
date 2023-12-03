const { app, BrowserWindow } = require('electron');
const path = require('path');

app.whenReady().then(() => {
  const mainWindow = new BrowserWindow({
    maximizable: false,

    width: 500,
    height: 350,
    backgroundColor: '#333',
    // frame: false,
    autoHideMenuBar: true,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  mainWindow.loadFile('index.html');
});
