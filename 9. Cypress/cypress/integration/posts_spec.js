describe('Testy JSONPlaceholder', function() {
    it('Pobiera posty', function() {
        cy.request('/posts')
            .should((response) => {
                expect(response.status).to.eq(200)
                expect(response.body).to.have.length(100)
                expect(response).to.have.property('headers')
                expect(response).to.have.property('duration')
            })
    })

    it('Pobiera pojedynczy post', function() {
        cy.request('/posts/1')
            .should((response) => {
                expect(response.status).to.eq(200)
                expect(response.body).to.have.property('id', 1)
            })
    })

    it('Tworzy nowy post', function() {
        const newItem = {
            title: 'foo',
            body: 'bar',
            userId: 1
        }

        cy.request('POST', '/posts', newItem)
            .then((response) => {
                expect(response.status).to.eq(201)
                expect(response.body).to.have.property('title', 'foo')
            })
    })
})
