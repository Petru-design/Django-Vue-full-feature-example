{  
    moduleCache: {
        vue: Vue,
    },
    
    delimiters: ['[[',']]'],
  
    getFile(url) {
        return fetch(url).then(response => {
                                  if (response.ok) {
                                      return response.text()
                                  } else {Promise.reject(response)}
                                });
    },
  
    addStyle(styleStr) {
        const style = document.createElement('style');
        style.textContent = styleStr;
        const ref = document.head.getElementsByTagName('style')[0] || null;
        document.head.insertBefore(style, ref);
    },
  
    log(type, ...args) {
        console.log(type, ...args);
    }
}