import pygame
import sys
import time

from objects.bullet import Bullet
from objects.alien import Alien
from misc import ControlsMisc


class Controls(ControlsMisc):

    def __init__(self):
        pygame.mixer.init()
        self.STOPPED_PLAYING = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.STOPPED_PLAYING)
        self.music_counter = 0

    def events(self, screen, starship, bullets):
        """Обработка событий."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Вправо
                if event.key == pygame.K_RIGHT:
                    starship.move_right = True
                # Влево
                elif event.key == pygame.K_LEFT:
                    starship.move_left = True
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(self.WOO_SOUND)).set_volume(self.STARSHIP_VOLUME)
                    new_bullet = Bullet(screen=screen, starship=starship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                # Вправо
                if event.key == pygame.K_RIGHT:
                    starship.move_right = False
                # Влево
                elif event.key == pygame.K_LEFT:
                    starship.move_left = False
            # Беспрерывное воспроизведение музыки
            if event.type == self.STOPPED_PLAYING:
                if self.music_counter < len(self.MAIN_MUSIC_PLAYLIST):
                    pygame.mixer.music.load(self.MAIN_MUSIC_PLAYLIST[self.music_counter])
                    pygame.mixer.music.play()
                    self.music_counter += 1
                elif self.music_counter == len(self.MAIN_MUSIC_PLAYLIST):
                    self.music_counter = 0
                    pygame.mixer.music.load(self.MAIN_MUSIC_PLAYLIST[self.music_counter])
                    pygame.mixer.music.play()
                    self.music_counter += 1

    def update(self, screen, starship, bullets, aliens, score, selected_background):
        """Обновление экрана."""
        screen.blit(pygame.image.load(self.BACKGROUND_IMAGES.get(selected_background)), (0, 0))
        score.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        starship.output()
        aliens.draw(screen)
        pygame.display.flip()

    def defeat(self, screen, aliens, bullets, selected_background):
        """Проигрыш."""
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(pygame.mixer.Sound(self.DEFEAT_SOUND)).set_volume(self.ADDITIONAL_VOLUME)
        aliens.empty()
        bullets.empty()
        screen.blit(pygame.image.load(self.BACKGROUND_IMAGES.get(selected_background)), (0, 0))
        image = pygame.image.load(self.DEFEAT_IMAGE)
        image_rect = image.get_rect(center=screen.get_rect().center)
        screen.blit(image, image_rect)
        pygame.display.flip()

    def update_bullets(self, screen, aliens, bullets, stats, score, difficulty_level):
        """Обновление позиций пуль."""
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            for alien in collisions.values():
                stats.score += int(difficulty_level * 1000 * len(alien))
            score.image_score()
            self.check_high_score(stats=stats, score=score)
            score.image_lives()

        if len(aliens) == 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.AMAZING_SOUND)).set_volume(self.ADDITIONAL_VOLUME)
            stats.level += self.INCREMENT_LEVEL
            score.image_level()
            self.ALIENS_MOVE_SPEED += difficulty_level
            bullets.empty()
            self.create_army(screen=screen, aliens=aliens)

    def starship_death(self, stats, screen, starship, aliens, bullets, score, selected_background):
        """Столкновение корабля и армии."""
        if stats.starship_left > 0:
            stats.starship_left -= 1
            score.image_lives()
            aliens.empty()
            bullets.empty()
            self.create_army(screen=screen, aliens=aliens)
            starship.create_starship()
            time.sleep(self.WAIT_TIME_BETWEEN_LIVES)
        else:
            stats.run_game = False
            self.defeat(screen=screen, aliens=aliens, bullets=bullets, selected_background=selected_background)

    def aliens_check(self, stats, screen, starship, aliens, bullets, score, selected_background):
        """Проверка, дошла ли армия до края экрана."""
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.starship_death(stats=stats, screen=screen, starship=starship, aliens=aliens, bullets=bullets,
                                    score=score, selected_background=selected_background)
                break

    def update_aliens(self, stats, screen, starship, aliens, bullets, score, selected_background):
        """Обновляет позицию прешельцев."""
        aliens.update()
        if pygame.sprite.spritecollideany(starship, aliens):
            self.starship_death(stats=stats, screen=screen, starship=starship,
                                aliens=aliens, bullets=bullets, score=score, selected_background=selected_background)
        self.aliens_check(stats=stats, screen=screen, starship=starship,
                          aliens=aliens, bullets=bullets, score=score, selected_background=selected_background)

    def create_army(self, screen, aliens):
        """Создание армии пришельцев."""
        alien = Alien(screen=screen)
        alien_width = alien.rect.width + alien.rect.width / 2
        alien_x_quantity = int((self.DISPLAY_SIZE[0] - 2 * alien_width) / alien_width)
        alien_height = alien.rect.height + alien.rect.width / 2
        alien_y_quantity = int((self.DISPLAY_SIZE[1] - self.STARSHIP_SIZE[1] - 2 * alien_height) / alien_height)

        for row_number in range(alien_y_quantity - 2):
            for string_number in range(alien_x_quantity):
                alien = Alien(screen=screen, move_speed=self.ALIENS_MOVE_SPEED)
                alien.x = alien_width + alien_width * string_number
                alien.y = alien_height + alien_height * row_number
                alien.rect.x = alien.x
                alien.rect.y = alien.rect.height + alien.rect.height * row_number
                aliens.add(alien)

    def check_high_score(self, stats, score):
        """Проверка новых рекордов."""
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            score.image_high_score()
            with open(self.HIGH_SCORE_FILE, 'w') as fileobject:
                fileobject.write(str(stats.high_score))
