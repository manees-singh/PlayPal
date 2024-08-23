const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const config = require('./config');


// Import routes

const authRoutes = require('./routes/auth');

// making express as an object.
const app = express();

//Middleware

app.use(cors()); // enables cors globally for all routes

