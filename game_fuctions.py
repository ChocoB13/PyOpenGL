from foods import Food
from random import choice
from math import dist
from time import sleep


def creat_foods(foods, gm_settings):
    objs = [['obj_files/friedegg.obj', 'texture/ovo.jpg'], ['obj_files/meat.obj', 'texture/crn.jpg']]
    if gm_settings.food_number < 10:
        obj = choice(objs)
        food = Food(obj[0], obj[1], gm_settings)
        foods.add(food.mesh)
        gm_settings.food_number += 1


def creat_objects(objects, gm_settings):
    objs = [['obj_files/colher.obj', 'texture/aluminio2.jpg'], ['obj_files/rolomassa.obj', 'texture/plywood_diff_4k.jpg']]
    if gm_settings.object_number < 6:
        obj = choice(objs)
        object = Food(obj[0], obj[1], gm_settings)
        objects.add(object.mesh)
        gm_settings.object_number += 1


def check_colisions_foods(foods, p_obj, pontuation):
    for food in foods.children_list:
        distn = dist([p_obj.global_position[0], p_obj.global_position[-1]], [food.global_position[0], food.global_position[-1]])
        if distn < 0.5 and food.global_position[1] < p_obj.global_position[1]:
            foods.remove(food)
            pontuation.ponto += 1


def remove_olds(foods, objects, stats):
    for food in foods.children_list:
        if food.global_position[1] < -3:
            foods.remove(food)
            #remove_all_items(foods, objects)
            stats.vidas_left -= 1
            #print(stats.vidas_left)
            #creat_foods(foods, gm_settings)
            #creat_objects(objects, gm_settings)
    for object in objects.children_list:
        if object.global_position[1] < -3:
            objects.remove(object)


def remove_all_objects(foods, objects):
    for food in foods.children_list:
            foods.remove(food)
    for object in objects.children_list:
        objects.remove(object)


def life_loss(foods, objects, stats, gm_settings):
    if stats.vidas_left > 0:
        stats.vidas_left -= 1
        remove_all_objects(foods, objects)
        """for food in foods.children_list:
            foods.remove(food)
        for object in objects.children_list:
            objects.remove(object)"""
        creat_foods(foods, gm_settings)
        creat_objects(objects, gm_settings)
    else:
        stats.game_ative = False


def check_colisions_objects(objects, p_obj, stats):
    for object in objects.children_list:
        distn = dist([p_obj.global_position[0], p_obj.global_position[-1]], [object.global_position[0], object.global_position[-1]])
        if distn < 0.5 and object.global_position[1] < p_obj.global_position[1]:
            #remove_all_items(foods, objects)
            objects.remove(object)
            stats.vidas_left -= 1
            #print(stats.vidas_left)
            #creat_foods(foods, gm_settings)
            #creat_objects(objects, gm_settings)

