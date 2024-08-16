require('dotenv').config();

module.exports={
  spoftifyClientId: process.env.SPOTIFY_CLIENT_ID,
  spotifyClientSecret: process.env.SPOTIFY_CLIENT_SECRET,
  redirectUrl: process.env.REDIRECT_URI,
  port: process.env.PORT

};