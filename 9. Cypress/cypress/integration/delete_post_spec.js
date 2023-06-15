describe('Test usuwania posta', function() {
    it('Usuwa post', function() {
        cy.request('DELETE', '/posts/1')
            .then((response) => {
                expect(response.status).to.eq(200)
            })
    })
})
