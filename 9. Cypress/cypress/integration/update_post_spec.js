describe('Test aktualizacji posta', function() {
    it('Aktualizuje post', function() {
        const updatedItem = {
            id: 1,
            title: 'foo updated',
            body: 'bar updated',
            userId: 1
        }

        cy.request('PUT', '/posts/1', updatedItem)
            .then((response) => {
                expect(response.status).to.eq(200)
                expect(response.body).to.have.property('title', 'foo updated')
            })
    })
})
