import pygame
import math

pygame.init()

my_font = pygame.font.SysFont('Monaco', 30)

class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def draw(self, screen, center, radius):
        pygame.draw.circle(screen, pygame.Color('red'), center, radius)
        text_surface = my_font.render(str(self.value), True, pygame.Color('black'))
        screen.blit(text_surface, text_surface.get_rect(center=center))


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * (i + 1)


class BST:

    # recursively creates BST from a sorted list and returns root node
    # time: O(n), space: O(lg(n))
    @staticmethod
    def create_BST_from_sorted_list(A: list):
        if not len(A):
            return None

        root = Node(A[len(A) // 2])
        root.right = BST.create_BST_from_sorted_list(A[len(A) // 2 + 1:])
        root.left = BST.create_BST_from_sorted_list(A[:len(A) // 2])

        return root

    def __init__(self, A: list):
        A.sort()
        self.array = A
        if not len(A):
            self.root = None
            self.h = -1
            return

        self.root = BST.create_BST_from_sorted_list(A)

        self.h = 1 + int(math.log2(len(A)))

    # uses two stacks to iteratively traverse the binary tree and print each node out
    def visualize(self, screen: pygame.Surface, header):
        w, h = screen.get_size()
        h -= header

        radius = min(w / (2 ** self.h), h / (2 * self.h), 50)

        s = [[self.root, (0, 0)]]
        s2 = [(0, len(self.array))]
        while len(s):
            curr, curr2 = s[-1][0], s2[-1]
            i, j = s[-1][1][0], s[-1][1][1]

            s.pop()
            s2.pop()

            if curr is None:
                continue

            if curr.left:
                pygame.draw.line(screen, pygame.Color('red'),
                                 ((j + 1 / 2) * w / (2 ** i), header + (i + 1 / 2) * h / self.h)
                                 , ((j * 2 + 1 / 2) * w / (2 ** (i + 1)), header + (i + 3 / 2) * h / self.h), 5)
            if curr.right:
                pygame.draw.line(screen, pygame.Color('red'),
                                 ((j + 1 / 2) * w / (2 ** i), header + (i + 1 / 2) * h / self.h)
                                 , ((j * 2 + 3 / 2) * w / (2 ** (i + 1)), header + (i + 3 / 2) * h / self.h), 5)

            curr.draw(screen, ((j + 1 / 2) * w / (2 ** i), header + (i + 1 / 2) * h / self.h), radius)

            s.append([curr.right, (i + 1, j * 2 + 1)])
            s.append([curr.left, (i + 1, j * 2)])

            s2.append(((curr2[0] + curr2[1]) // 2 + 1, curr2[1]))
            s2.append((curr2[0], (curr2[0] + curr2[1]) // 2))
