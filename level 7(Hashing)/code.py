import numpy as np
import random
PI_MAPPING = {
        (0, 0, 0) : (0, 0, 0),
        (0, 0, 1) : (0, 0, 1),
        (0, 0, 2) : (0, 0, 2),
        (0, 0, 3) : (0, 0, 3),
        (0, 0, 4) : (0, 0, 4),
        (0, 0, 5) : (0, 0, 5),
        (0, 0, 6) : (0, 0, 6),
        (0, 0, 7) : (0, 0, 7),
        (0, 1, 0) : (3, 0, 0),
        (0, 1, 1) : (3, 0, 1),
        (0, 1, 2) : (3, 0, 2),
        (0, 1, 3) : (3, 0, 3),
        (0, 1, 4) : (3, 0, 4),
        (0, 1, 5) : (3, 0, 5),
        (0, 1, 6) : (3, 0, 6),
        (0, 1, 7) : (3, 0, 7),
        (0, 2, 0) : (1, 0, 0),
        (0, 2, 1) : (1, 0, 1),
        (0, 2, 2) : (1, 0, 2),
        (0, 2, 3) : (1, 0, 3),
        (0, 2, 4) : (1, 0, 4),
        (0, 2, 5) : (1, 0, 5),
        (0, 2, 6) : (1, 0, 6),
        (0, 2, 7) : (1, 0, 7),
        (0, 3, 0) : (4, 0, 0),
        (0, 3, 1) : (4, 0, 1),
        (0, 3, 2) : (4, 0, 2),
        (0, 3, 3) : (4, 0, 3),
        (0, 3, 4) : (4, 0, 4),
        (0, 3, 5) : (4, 0, 5),
        (0, 3, 6) : (4, 0, 6),
        (0, 3, 7) : (4, 0, 7),
        (0, 4, 0) : (2, 0, 0),
        (0, 4, 1) : (2, 0, 1),
        (0, 4, 2) : (2, 0, 2),
        (0, 4, 3) : (2, 0, 3),
        (0, 4, 4) : (2, 0, 4),
        (0, 4, 5) : (2, 0, 5),
        (0, 4, 6) : (2, 0, 6),
        (0, 4, 7) : (2, 0, 7),
        (1, 0, 0) : (1, 1, 0),
        (1, 0, 1) : (1, 1, 1),
        (1, 0, 2) : (1, 1, 2),
        (1, 0, 3) : (1, 1, 3),
        (1, 0, 4) : (1, 1, 4),
        (1, 0, 5) : (1, 1, 5),
        (1, 0, 6) : (1, 1, 6),
        (1, 0, 7) : (1, 1, 7),
        (1, 1, 0) : (4, 1, 0),
        (1, 1, 1) : (4, 1, 1),
        (1, 1, 2) : (4, 1, 2),
        (1, 1, 3) : (4, 1, 3),
        (1, 1, 4) : (4, 1, 4),
        (1, 1, 5) : (4, 1, 5),
        (1, 1, 6) : (4, 1, 6),
        (1, 1, 7) : (4, 1, 7),
        (1, 2, 0) : (2, 1, 0),
        (1, 2, 1) : (2, 1, 1),
        (1, 2, 2) : (2, 1, 2),
        (1, 2, 3) : (2, 1, 3),
        (1, 2, 4) : (2, 1, 4),
        (1, 2, 5) : (2, 1, 5),
        (1, 2, 6) : (2, 1, 6),
        (1, 2, 7) : (2, 1, 7),
        (1, 3, 0) : (0, 1, 0),
        (1, 3, 1) : (0, 1, 1),
        (1, 3, 2) : (0, 1, 2),
        (1, 3, 3) : (0, 1, 3),
        (1, 3, 4) : (0, 1, 4),
        (1, 3, 5) : (0, 1, 5),
        (1, 3, 6) : (0, 1, 6),
        (1, 3, 7) : (0, 1, 7),
        (1, 4, 0) : (3, 1, 0),
        (1, 4, 1) : (3, 1, 1),
        (1, 4, 2) : (3, 1, 2),
        (1, 4, 3) : (3, 1, 3),
        (1, 4, 4) : (3, 1, 4),
        (1, 4, 5) : (3, 1, 5),
        (1, 4, 6) : (3, 1, 6),
        (1, 4, 7) : (3, 1, 7),
        (2, 0, 0) : (2, 2, 0),
        (2, 0, 1) : (2, 2, 1),
        (2, 0, 2) : (2, 2, 2),
        (2, 0, 3) : (2, 2, 3),
        (2, 0, 4) : (2, 2, 4),
        (2, 0, 5) : (2, 2, 5),
        (2, 0, 6) : (2, 2, 6),
        (2, 0, 7) : (2, 2, 7),
        (2, 1, 0) : (0, 2, 0),
        (2, 1, 1) : (0, 2, 1),
        (2, 1, 2) : (0, 2, 2),
        (2, 1, 3) : (0, 2, 3),
        (2, 1, 4) : (0, 2, 4),
        (2, 1, 5) : (0, 2, 5),
        (2, 1, 6) : (0, 2, 6),
        (2, 1, 7) : (0, 2, 7),
        (2, 2, 0) : (3, 2, 0),
        (2, 2, 1) : (3, 2, 1),
        (2, 2, 2) : (3, 2, 2),
        (2, 2, 3) : (3, 2, 3),
        (2, 2, 4) : (3, 2, 4),
        (2, 2, 5) : (3, 2, 5),
        (2, 2, 6) : (3, 2, 6),
        (2, 2, 7) : (3, 2, 7),
        (2, 3, 0) : (1, 2, 0),
        (2, 3, 1) : (1, 2, 1),
        (2, 3, 2) : (1, 2, 2),
        (2, 3, 3) : (1, 2, 3),
        (2, 3, 4) : (1, 2, 4),
        (2, 3, 5) : (1, 2, 5),
        (2, 3, 6) : (1, 2, 6),
        (2, 3, 7) : (1, 2, 7),
        (2, 4, 0) : (4, 2, 0),
        (2, 4, 1) : (4, 2, 1),
        (2, 4, 2) : (4, 2, 2),
        (2, 4, 3) : (4, 2, 3),
        (2, 4, 4) : (4, 2, 4),
        (2, 4, 5) : (4, 2, 5),
        (2, 4, 6) : (4, 2, 6),
        (2, 4, 7) : (4, 2, 7),
        (3, 0, 0) : (3, 3, 0),
        (3, 0, 1) : (3, 3, 1),
        (3, 0, 2) : (3, 3, 2),
        (3, 0, 3) : (3, 3, 3),
        (3, 0, 4) : (3, 3, 4),
        (3, 0, 5) : (3, 3, 5),
        (3, 0, 6) : (3, 3, 6),
        (3, 0, 7) : (3, 3, 7),
        (3, 1, 0) : (1, 3, 0),
        (3, 1, 1) : (1, 3, 1),
        (3, 1, 2) : (1, 3, 2),
        (3, 1, 3) : (1, 3, 3),
        (3, 1, 4) : (1, 3, 4),
        (3, 1, 5) : (1, 3, 5),
        (3, 1, 6) : (1, 3, 6),
        (3, 1, 7) : (1, 3, 7),
        (3, 2, 0) : (4, 3, 0),
        (3, 2, 1) : (4, 3, 1),
        (3, 2, 2) : (4, 3, 2),
        (3, 2, 3) : (4, 3, 3),
        (3, 2, 4) : (4, 3, 4),
        (3, 2, 5) : (4, 3, 5),
        (3, 2, 6) : (4, 3, 6),
        (3, 2, 7) : (4, 3, 7),
        (3, 3, 0) : (2, 3, 0),
        (3, 3, 1) : (2, 3, 1),
        (3, 3, 2) : (2, 3, 2),
        (3, 3, 3) : (2, 3, 3),
        (3, 3, 4) : (2, 3, 4),
        (3, 3, 5) : (2, 3, 5),
        (3, 3, 6) : (2, 3, 6),
        (3, 3, 7) : (2, 3, 7),
        (3, 4, 0) : (0, 3, 0),
        (3, 4, 1) : (0, 3, 1),
        (3, 4, 2) : (0, 3, 2),
        (3, 4, 3) : (0, 3, 3),
        (3, 4, 4) : (0, 3, 4),
        (3, 4, 5) : (0, 3, 5),
        (3, 4, 6) : (0, 3, 6),
        (3, 4, 7) : (0, 3, 7),
        (4, 0, 0) : (4, 4, 0),
        (4, 0, 1) : (4, 4, 1),
        (4, 0, 2) : (4, 4, 2),
        (4, 0, 3) : (4, 4, 3),
        (4, 0, 4) : (4, 4, 4),
        (4, 0, 5) : (4, 4, 5),
        (4, 0, 6) : (4, 4, 6),
        (4, 0, 7) : (4, 4, 7),
        (4, 1, 0) : (2, 4, 0),
        (4, 1, 1) : (2, 4, 1),
        (4, 1, 2) : (2, 4, 2),
        (4, 1, 3) : (2, 4, 3),
        (4, 1, 4) : (2, 4, 4),
        (4, 1, 5) : (2, 4, 5),
        (4, 1, 6) : (2, 4, 6),
        (4, 1, 7) : (2, 4, 7),
        (4, 2, 0) : (0, 4, 0),
        (4, 2, 1) : (0, 4, 1),
        (4, 2, 2) : (0, 4, 2),
        (4, 2, 3) : (0, 4, 3),
        (4, 2, 4) : (0, 4, 4),
        (4, 2, 5) : (0, 4, 5),
        (4, 2, 6) : (0, 4, 6),
        (4, 2, 7) : (0, 4, 7),
        (4, 3, 0) : (3, 4, 0),
        (4, 3, 1) : (3, 4, 1),
        (4, 3, 2) : (3, 4, 2),
        (4, 3, 3) : (3, 4, 3),
        (4, 3, 4) : (3, 4, 4),
        (4, 3, 5) : (3, 4, 5),
        (4, 3, 6) : (3, 4, 6),
        (4, 3, 7) : (3, 4, 7),
        (4, 4, 0) : (1, 4, 0),
        (4, 4, 1) : (1, 4, 1),
        (4, 4, 2) : (1, 4, 2),
        (4, 4, 3) : (1, 4, 3),
        (4, 4, 4) : (1, 4, 4),
        (4, 4, 5) : (1, 4, 5),
        (4, 4, 6) : (1, 4, 6),
        (4, 4, 7) : (1, 4, 7),
}


PI_INVERSE_MAPPING = {
        (0, 0, 0) : (0, 0, 0),
        (0, 0, 1) : (0, 0, 1),
        (0, 0, 2) : (0, 0, 2),
        (0, 0, 3) : (0, 0, 3),
        (0, 0, 4) : (0, 0, 4),
        (0, 0, 5) : (0, 0, 5),
        (0, 0, 6) : (0, 0, 6),
        (0, 0, 7) : (0, 0, 7),
        (3, 0, 0) : (0, 1, 0),
        (3, 0, 1) : (0, 1, 1),
        (3, 0, 2) : (0, 1, 2),
        (3, 0, 3) : (0, 1, 3),
        (3, 0, 4) : (0, 1, 4),
        (3, 0, 5) : (0, 1, 5),
        (3, 0, 6) : (0, 1, 6),
        (3, 0, 7) : (0, 1, 7),
        (1, 0, 0) : (0, 2, 0),
        (1, 0, 1) : (0, 2, 1),
        (1, 0, 2) : (0, 2, 2),
        (1, 0, 3) : (0, 2, 3),
        (1, 0, 4) : (0, 2, 4),
        (1, 0, 5) : (0, 2, 5),
        (1, 0, 6) : (0, 2, 6),
        (1, 0, 7) : (0, 2, 7),
        (4, 0, 0) : (0, 3, 0),
        (4, 0, 1) : (0, 3, 1),
        (4, 0, 2) : (0, 3, 2),
        (4, 0, 3) : (0, 3, 3),
        (4, 0, 4) : (0, 3, 4),
        (4, 0, 5) : (0, 3, 5),
        (4, 0, 6) : (0, 3, 6),
        (4, 0, 7) : (0, 3, 7),
        (2, 0, 0) : (0, 4, 0),
        (2, 0, 1) : (0, 4, 1),
        (2, 0, 2) : (0, 4, 2),
        (2, 0, 3) : (0, 4, 3),
        (2, 0, 4) : (0, 4, 4),
        (2, 0, 5) : (0, 4, 5),
        (2, 0, 6) : (0, 4, 6),
        (2, 0, 7) : (0, 4, 7),
        (1, 1, 0) : (1, 0, 0),
        (1, 1, 1) : (1, 0, 1),
        (1, 1, 2) : (1, 0, 2),
        (1, 1, 3) : (1, 0, 3),
        (1, 1, 4) : (1, 0, 4),
        (1, 1, 5) : (1, 0, 5),
        (1, 1, 6) : (1, 0, 6),
        (1, 1, 7) : (1, 0, 7),
        (4, 1, 0) : (1, 1, 0),
        (4, 1, 1) : (1, 1, 1),
        (4, 1, 2) : (1, 1, 2),
        (4, 1, 3) : (1, 1, 3),
        (4, 1, 4) : (1, 1, 4),
        (4, 1, 5) : (1, 1, 5),
        (4, 1, 6) : (1, 1, 6),
        (4, 1, 7) : (1, 1, 7),
        (2, 1, 0) : (1, 2, 0),
        (2, 1, 1) : (1, 2, 1),
        (2, 1, 2) : (1, 2, 2),
        (2, 1, 3) : (1, 2, 3),
        (2, 1, 4) : (1, 2, 4),
        (2, 1, 5) : (1, 2, 5),
        (2, 1, 6) : (1, 2, 6),
        (2, 1, 7) : (1, 2, 7),
        (0, 1, 0) : (1, 3, 0),
        (0, 1, 1) : (1, 3, 1),
        (0, 1, 2) : (1, 3, 2),
        (0, 1, 3) : (1, 3, 3),
        (0, 1, 4) : (1, 3, 4),
        (0, 1, 5) : (1, 3, 5),
        (0, 1, 6) : (1, 3, 6),
        (0, 1, 7) : (1, 3, 7),
        (3, 1, 0) : (1, 4, 0),
        (3, 1, 1) : (1, 4, 1),
        (3, 1, 2) : (1, 4, 2),
        (3, 1, 3) : (1, 4, 3),
        (3, 1, 4) : (1, 4, 4),
        (3, 1, 5) : (1, 4, 5),
        (3, 1, 6) : (1, 4, 6),
        (3, 1, 7) : (1, 4, 7),
        (2, 2, 0) : (2, 0, 0),
        (2, 2, 1) : (2, 0, 1),
        (2, 2, 2) : (2, 0, 2),
        (2, 2, 3) : (2, 0, 3),
        (2, 2, 4) : (2, 0, 4),
        (2, 2, 5) : (2, 0, 5),
        (2, 2, 6) : (2, 0, 6),
        (2, 2, 7) : (2, 0, 7),
        (0, 2, 0) : (2, 1, 0),
        (0, 2, 1) : (2, 1, 1),
        (0, 2, 2) : (2, 1, 2),
        (0, 2, 3) : (2, 1, 3),
        (0, 2, 4) : (2, 1, 4),
        (0, 2, 5) : (2, 1, 5),
        (0, 2, 6) : (2, 1, 6),
        (0, 2, 7) : (2, 1, 7),
        (3, 2, 0) : (2, 2, 0),
        (3, 2, 1) : (2, 2, 1),
        (3, 2, 2) : (2, 2, 2),
        (3, 2, 3) : (2, 2, 3),
        (3, 2, 4) : (2, 2, 4),
        (3, 2, 5) : (2, 2, 5),
        (3, 2, 6) : (2, 2, 6),
        (3, 2, 7) : (2, 2, 7),
        (1, 2, 0) : (2, 3, 0),
        (1, 2, 1) : (2, 3, 1),
        (1, 2, 2) : (2, 3, 2),
        (1, 2, 3) : (2, 3, 3),
        (1, 2, 4) : (2, 3, 4),
        (1, 2, 5) : (2, 3, 5),
        (1, 2, 6) : (2, 3, 6),
        (1, 2, 7) : (2, 3, 7),
        (4, 2, 0) : (2, 4, 0),
        (4, 2, 1) : (2, 4, 1),
        (4, 2, 2) : (2, 4, 2),
        (4, 2, 3) : (2, 4, 3),
        (4, 2, 4) : (2, 4, 4),
        (4, 2, 5) : (2, 4, 5),
        (4, 2, 6) : (2, 4, 6),
        (4, 2, 7) : (2, 4, 7),
        (3, 3, 0) : (3, 0, 0),
        (3, 3, 1) : (3, 0, 1),
        (3, 3, 2) : (3, 0, 2),
        (3, 3, 3) : (3, 0, 3),
        (3, 3, 4) : (3, 0, 4),
        (3, 3, 5) : (3, 0, 5),
        (3, 3, 6) : (3, 0, 6),
        (3, 3, 7) : (3, 0, 7),
        (1, 3, 0) : (3, 1, 0),
        (1, 3, 1) : (3, 1, 1),
        (1, 3, 2) : (3, 1, 2),
        (1, 3, 3) : (3, 1, 3),
        (1, 3, 4) : (3, 1, 4),
        (1, 3, 5) : (3, 1, 5),
        (1, 3, 6) : (3, 1, 6),
        (1, 3, 7) : (3, 1, 7),
        (4, 3, 0) : (3, 2, 0),
        (4, 3, 1) : (3, 2, 1),
        (4, 3, 2) : (3, 2, 2),
        (4, 3, 3) : (3, 2, 3),
        (4, 3, 4) : (3, 2, 4),
        (4, 3, 5) : (3, 2, 5),
        (4, 3, 6) : (3, 2, 6),
        (4, 3, 7) : (3, 2, 7),
        (2, 3, 0) : (3, 3, 0),
        (2, 3, 1) : (3, 3, 1),
        (2, 3, 2) : (3, 3, 2),
        (2, 3, 3) : (3, 3, 3),
        (2, 3, 4) : (3, 3, 4),
        (2, 3, 5) : (3, 3, 5),
        (2, 3, 6) : (3, 3, 6),
        (2, 3, 7) : (3, 3, 7),
        (0, 3, 0) : (3, 4, 0),
        (0, 3, 1) : (3, 4, 1),
        (0, 3, 2) : (3, 4, 2),
        (0, 3, 3) : (3, 4, 3),
        (0, 3, 4) : (3, 4, 4),
        (0, 3, 5) : (3, 4, 5),
        (0, 3, 6) : (3, 4, 6),
        (0, 3, 7) : (3, 4, 7),
        (4, 4, 0) : (4, 0, 0),
        (4, 4, 1) : (4, 0, 1),
        (4, 4, 2) : (4, 0, 2),
        (4, 4, 3) : (4, 0, 3),
        (4, 4, 4) : (4, 0, 4),
        (4, 4, 5) : (4, 0, 5),
        (4, 4, 6) : (4, 0, 6),
        (4, 4, 7) : (4, 0, 7),
        (2, 4, 0) : (4, 1, 0),
        (2, 4, 1) : (4, 1, 1),
        (2, 4, 2) : (4, 1, 2),
        (2, 4, 3) : (4, 1, 3),
        (2, 4, 4) : (4, 1, 4),
        (2, 4, 5) : (4, 1, 5),
        (2, 4, 6) : (4, 1, 6),
        (2, 4, 7) : (4, 1, 7),
        (0, 4, 0) : (4, 2, 0),
        (0, 4, 1) : (4, 2, 1),
        (0, 4, 2) : (4, 2, 2),
        (0, 4, 3) : (4, 2, 3),
        (0, 4, 4) : (4, 2, 4),
        (0, 4, 5) : (4, 2, 5),
        (0, 4, 6) : (4, 2, 6),
        (0, 4, 7) : (4, 2, 7),
        (3, 4, 0) : (4, 3, 0),
        (3, 4, 1) : (4, 3, 1),
        (3, 4, 2) : (4, 3, 2),
        (3, 4, 3) : (4, 3, 3),
        (3, 4, 4) : (4, 3, 4),
        (3, 4, 5) : (4, 3, 5),
        (3, 4, 6) : (4, 3, 6),
        (3, 4, 7) : (4, 3, 7),
        (1, 4, 0) : (4, 4, 0),
        (1, 4, 1) : (4, 4, 1),
        (1, 4, 2) : (4, 4, 2),
        (1, 4, 3) : (4, 4, 3),
        (1, 4, 4) : (4, 4, 4),
        (1, 4, 5) : (4, 4, 5),
        (1, 4, 6) : (4, 4, 6),
        (1, 4, 7) : (4, 4, 7),
}

DIM_X = 5
DIM_Y = 5
DIM_Z = 8

CHI_MAPPING = {
        '00000':'00000',
        '00001':'00101',
        '00010':'01010',
        '00011':'01011',
        '00100':'10100',
        '00101':'10001',
        '00110':'10110',
        '00111':'10111',
        '01000':'01001',
        '01001':'01100',
        '01010':'00011',
        '01011':'00010',
        '01100':'01101',
        '01101':'01000',
        '01110':'01111',
        '01111':'01110',
        '10000':'10010',
        '10001':'10101',
        '10010':'11000',
        '10011':'11011',
        '10100':'00110',
        '10101':'00001',
        '10110':'00100',
        '10111':'00111',
        '11000':'11010',
        '11001':'11101',
        '11010':'10000',
        '11011':'10011',
        '11100':'11110',
        '11101':'11001',
        '11110':'11100',
        '11111':'11111',
        }
CHI_MAPPING_INVERSE = {
        '00000':'00000',
        '00101':'00001',
        '01010':'00010',
        '01011':'00011',
        '10100':'00100',
        '10001':'00101',
        '10110':'00110',
        '10111':'00111',
        '01001':'01000',
        '01100':'01001',
        '00011':'01010',
        '00010':'01011',
        '01101':'01100',
        '01000':'01101',
        '01111':'01110',
        '01110':'01111',
        '10010':'10000',
        '10101':'10001',
        '11000':'10010',
        '11011':'10011',
        '00110':'10100',
        '00001':'10101',
        '00100':'10110',
        '00111':'10111',
        '11010':'11000',
        '11101':'11001',
        '10000':'11010',
        '10011':'11011',
        '11110':'11100',
        '11001':'11101',
        '11100':'11110',
        '11111':'11111',
        }


def block_xor(block, msg):
    assert (len(msg) == 184), "Length of msg block should be 184 bits"
    msg+="0"*16
    for x in range(DIM_X):
        for y in range(DIM_Y):
            for z in range(DIM_Z):
                block[x,y,z] ^= int(msg[DIM_Z*(5*y+x)+z])
    return block

def chi(block):
    for y in range(DIM_Y):
        for z in range(DIM_Z):
            ret = CHI_MAPPING[''.join([str(elem) for elem in block[:,y,z]])]
            block[:,y,z] = [int(elem) for elem in ret]
    return block

def rho(block):
    nblock = np.random.random_integers(0, 0, (DIM_X,DIM_Y,DIM_Z))
    nblock[0,0,:] = block[0,0,:]
    (x,y) = (1,0)
    for t in range(24):
        for z in range(DIM_Z):
            nblock[x,y,z] = block[x,y,(z-int((t+1)*(t+2)/2)+20*DIM_Z)%DIM_Z]
        (x,y) = (y,(2*x+3*y)%5)
    return nblock

def pi(block):
    nblock = np.random.random_integers(0, 0, (DIM_X,DIM_Y,DIM_Z))
    for x in range(DIM_X):
        for y in range(DIM_Y):
            for z in range(DIM_Z):
                (_x, _y, _z) = PI_MAPPING[(x,y,z)]
                nblock[x, y, z] = block[_x, _y, _z]
    return nblock

def theta(block):
    colsum_matrix = np.remainder(block.sum(axis=1), 2)
    res_matrix = []
    for x in range(DIM_X):
        res_array = []
        colsum_array1 = colsum_matrix[(x-1+DIM_X)%DIM_X]
        colsum_array2 = colsum_matrix[(x+1)%DIM_X]
        for y in range(DIM_X):
            res_col = []
            for z in range(DIM_Z):
                val = block[x,y,z]^colsum_array1[z%DIM_Z]^colsum_array2[(z-1)%DIM_Z]
                res_col.append(val)
            res_array.append(res_col)
        res_matrix.append(res_array)
    return np.array(res_matrix)

def round_function(block):
    block = chi(block)
    block = rho(block)
    block = pi(block)
    block = theta(block)
    return block

def weccakf(block, no_round = 2):
    for round_ind in range(no_round):
        block = round_function(block)
    return block

def chi_inverse(block):
    for y in range(DIM_Y):
        for z in range(DIM_Z):
            ret = CHI_MAPPING_INVERSE[''.join([str(elem) for elem in block[:,y,z]])]
            block[:,y,z] = [int(elem) for elem in ret]
    return block

def rho_inverse(block):
    nblock = np.random.random_integers(0, 0, (DIM_X,DIM_Y,DIM_Z))
    nblock[0,0,:] = block[0,0,:]
    (x,y) = (1,0)
    for t in range(24):
        for z in range(DIM_Z):
            nblock[x,y,z] = block[x,y,(z+int((t+1)*(t+2)/2))%DIM_Z]
        (x,y) = (y,(2*x+3*y)%5)
    return nblock

def pi_inverse(block):
    nblock = np.random.random_integers(0, 0, (DIM_X,DIM_Y,DIM_Z))
    for x in range(DIM_X):
        for y in range(DIM_Y):
            for z in range(DIM_Z):
                (_x, _y, _z) = PI_INVERSE_MAPPING[(x,y,z)]
                nblock[x, y, z] = block[_x, _y, _z]
    return nblock

def theta_inverse(block):
    base_layer = block[:,0,:]
    colsum_matrix = np.remainder(block.sum(axis=1), 2)
    rem_matrix = np.bitwise_xor(colsum_matrix, base_layer)
    l = []
    for res in range(2**DIM_X):
        soln = np.eye(DIM_X, DIM_Z, dtype='int')
        ans = [int(n) for n in ("{0:0" + str(DIM_X) + "b}").format(res)]
        soln[:, DIM_Z-1] = np.array(ans)
        for z in range(DIM_Z-2,-1,-1):
            for x in range(DIM_X):
                soln[x, z] = soln[(x-1+5)%DIM_X, (z+1)%DIM_Z] ^ soln[(x-2+5)%DIM_X, (z+1)%DIM_Z] \
                        ^ rem_matrix[(x-2+5)%DIM_X, (z+1)%DIM_Z] ^ rem_matrix[x,z] ^ \
                        base_layer[(x-1+5)%DIM_X, (z+1)%DIM_Z]
        z = DIM_Z-1
        temp = []
        for x in range(DIM_X):
            s  = soln[(x-1+5)%DIM_X, (z+1)%DIM_Z] ^ soln[(x-2+5)%DIM_X, (z+1)%DIM_Z] \
                    ^ rem_matrix[(x-2+5)%DIM_X, (z+1)%DIM_Z] ^ rem_matrix[x,z] ^ \
                    base_layer[(x-1+5)%DIM_X, (z+1)%DIM_Z]
            temp.append(s)
        if(np.sum(np.abs(np.array(temp) - soln[:,z])) == 0):
            l.append(soln[:, z])
    return l



def round_inverse(block):
    block = pi_inverse(block)
    block = rho_inverse(block)
    block = chi_inverse(block)
    return block


def weccakf_inverse(block, no_round=2):
    for r in range(no_round):
        block = round_inverse(block)
    return block
block_size = DIM_X * DIM_Y * DIM_Z
msg_size = block_size - 16
flags = [0]*(1<<16)
cnt = 0
random.seed()

cnt_lim = len(flags)

def get_block_digest(msg):
    assert len(msg) == block_size
    np_msg = np.array(msg)
    np_msg.resize(DIM_X, DIM_Y, DIM_Z)
    np_msg[3:,4,:] = 0

    np_digest = weccakf(np_msg)
    np_digest.resize(np_digest.size)

    digest_suffix = np_digest[msg_size:]
    ind = 0
    for i in digest_suffix:
        ind = (ind<<1)|i
    if not flags[ind]:
        global cnt
        cnt += 1
        flags[ind] = 1
def populate():
    print('# loops\t# hits')
    loop_count = 0
    prev_cnt = cnt
    while cnt < cnt_lim:
        try:
            msg = [random.randint(0,1) for i in range(block_size)]
            get_block_digest(msg)

            loop_count += 1

            if not (cnt&(cnt-1)):
                if cnt != prev_cnt:
                    print('{}\t{}'.format(loop_count, cnt))
                    prev_cnt = cnt
            elif not loop_count&(loop_count-1):
                print('{}\t{}'.format(loop_count, cnt))
                prev_cnt = cnt

        except KeyboardInterrupt:
            print(loop_count, cnt)

def utilities():
    ZERO = np.random.random_integers(0, 0, DIM_Z)
    for i in range(1000000):
        matrix = np.random.random_integers(0, 1, (DIM_X,DIM_Y,DIM_Z))
        matrix[3,4,:] = ZERO
        matrix[4,4,:] = ZERO
        soln = np.copy(matrix)
        block = weccakf(matrix, no_round=2)
        if(i%1000 == 0):
            print(i)
        if(np.sum(block[3,4,:]) == 0 and np.sum(block[4,4,:]) == 0):
            print(soln)
            input()

    R2_ANS = np.array(
    [[[0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1]],
                        
    [[1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1]],
                        
    [[1, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]],
                        
    [[0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]],
                        
    [[1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]]
    )

    R24_ANS = np.array(
    [[[0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1]],
                            
    [[1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0]],
                            
    [[1, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1]],
                            
    [[1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]],
                            
    [[0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]]
            )


if __name__ == "__main__":
    populate()
    utilities()