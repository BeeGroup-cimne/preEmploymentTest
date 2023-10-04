const { Router } = require('express');
const router = Router();

const { getData } = require('../controllers/index.controller');

router.get('/data', getData);
router.get('/', (req, res) => {
    // You can add logic here to render a specific HTML page or send a response
    // For example:
    res.sendFile(__dirname  + '/index.html');
  });

module.exports = router;