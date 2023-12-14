describe('Pruebas de estress register',()=>{
    it('registrar clientes repetidamente',()=>{
        //numero de vvecces que se va a realizar la accion
       const numberOfRepetitions = 10;
       for (let i=0; i <numberOfRepetitions; i++){
      
        // se visita la ruta de registro
       cy.visit('http://127.0.0.1:8000/registrar_cliente/');

       //se llama al formulario
       cy.get('input[name="nombre"]').type('nombre prueba');
       cy.get('input[name="direccion"]').type('direccion prueba');

       //envio de formulario
       cy.get('form').submit();

       //verificar la direccion
       cy.url().should('include','/registrar_cliente/')
    }
    })
})