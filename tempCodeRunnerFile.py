((
                    1 if event.button == 1 else 0
                ) if event.type == pygame.MOUSEBUTTONUP else 0
            ) for event in pygame.event.get()