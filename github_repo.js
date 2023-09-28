var https = require('https');

async function getRepos(username, token) {
    const headers = { 
      'User-Agent': 'node.js',
      'Authorization': 'token ' + token
    };
  
    let repos = [];
    for (let i = 1; i <= 6; i++) {
      const response = await fetch(`https://api.github.com/users/${username}/repos?type=all&per_page=100&page=${i}`, { headers });
      const data = await response.json();
      repos = repos.concat(data);
    }
  
    repos.forEach((repo) => {
      console.log(`
      {
        name:"${repo.name}",
        description:"${repo.description}"
      },
      `);
    });
  }
  

getRepos('beingofexistence', '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');
