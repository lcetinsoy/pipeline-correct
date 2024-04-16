describe('My First Test', () => {
    it('Does not do much!', () => {
      cy.visit('/home')
      cy.get('#formulaire').contains('login')
    })
})