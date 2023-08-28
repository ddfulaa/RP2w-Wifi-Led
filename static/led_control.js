document.getElementById("encenderLed").addEventListener("click", function() {
  fetch("on", {
      method: "POST",
      headers: {
          "Content-Type": "application/x-www-form-urlencoded"
      },
      body: "accion=encender"
  })
  .then(response => {
      if (response.ok) {
          return response.text(); // Convertir la respuesta a texto
      } else {
          throw new Error("Hubo un problema en la solicitud");
      }
  })
  .then(data => {
      console.log("Respuesta del servidor:", data);
      // Puedes hacer algo con los datos recibidos aquí
  })
  .catch(error => {
      console.error("Error:", error);
  });
});

document.getElementById("apagarLed").addEventListener("click", function() {
  fetch("off", {
      method: "POST",
      headers: {
          "Content-Type": "application/x-www-form-urlencoded"
      },
      body: "accion=apagar"
  })
  .then(response => {
      if (response.ok) {
          return response.text(); // Convertir la respuesta a texto
      } else {
          throw new Error("Hubo un problema en la solicitud");
      }
  })
  .then(data => {
      console.log("Respuesta del servidor:", data);
      // Puedes hacer algo con los datos recibidos aquí
  })
  .catch(error => {
      console.error("Error:", error);
  });
});