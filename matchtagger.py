import re
import click
import time
import os
import csv
import glob
from fuzzywuzzy import fuzz, process
timestr = time.strftime("%Y%m%d-%H%M%S")


@click.group()
@click.version_option(version='0.02', prog_name='matchtagger')
def main():
    """MatchTagger CLI :compares multiple files,match them and label them as tags"""

    pass


@main.command()
@click.argument('main_file')
def singlematch(main_file):
    """ Match File 1 with Keywords From Default List

    eg. matchtagger singlematch masterfile.txt 

    eg. python matchtager singlematch masterfile.txt

    """
    # List of Default Keywords
    keywords_file = {'pradaxa', 'gemcitabine', 'rivaroxaban', 'edoxa', 'xarelto', 'riva', 'edoxaban', 'eliquis',
                     'dabigatran', 'apix', 'savaysa', 'dabi', 'edox', 'apixaban', 'elliquis', 'coumadin', 'apixa', 'warfarin'}
    pos_keywords = {'continue', 'start', 'begin', 'use'}
    neg_keywords = {'discontinue', 'stop', 'hold'}

    # File Name
    results_file = "extracted_results" + timestr + '.csv'

    # Open and Match Files
    with open(os.path.join(main_file)) as master_file:
        with open(results_file, "a+") as finalfile:
            writer = csv.writer(finalfile)
            for line in master_file:
                line = re.sub(r'[^\x00-\x7F]+', ' ', line)
                if set(line.lower().split()[:-1]) & keywords_file:
                    click.echo('Found Match:: {}'.format(line))
                    matched_word = process.extract(
                        line, keywords_file, limit=1)
                    click.secho(
                        ('Match Word:: {}'.format(matched_word)), fg="yellow")
                    if set(line.lower().split()[:-1]) & pos_keywords:
                        click.secho(('Positive::{}'.format(line)), fg="blue")
                        label = "Positive"
                    elif set(line.lower().split()[:-1]) & neg_keywords:
                        click.secho(('Negative::{}'.format(line)), fg="red")
                        label = "Negative"
                    else:
                        label = 'Neutral'
                    result = '"Filename":"{}",\n"Matched_Sentence":"{}",\n"Label":"{}"\n'.format(
                        master_file.name, line, label)
                    print(result)
                    writer.writerow((main_file, line.strip(), label))
                    click.secho(
                        ('Finished Task For: {}'.format(line)), fg="blue")
                    click.secho(
                        ('Saved Result in File: {}'.format(results_file)), fg="blue")

                elif set(line.lower().split()[:-1]) not in keywords_file:
                    click.secho(('None Found::{}'.format(line)), fg="green")
                else:
                    click.secho(('Neutral::{}'.format(line)), fg="green")
                    label = "Neutral"


@main.command()
@click.argument('current_path')
def bulkmatch(current_path):
    """ Bulk Matching of File 1 with Keywords From 3 Files

    eg. matchtagger bulkmatch .

    eg. python matchtagger bulkmatch .

    """
    # List of Default Keywords
    keywords_file = {'pradaxa', 'gemcitabine', 'rivaroxaban', 'edoxa', 'xarelto', 'riva', 'edoxaban', 'eliquis',
                     'dabigatran', 'apix', 'savaysa', 'dabi', 'edox', 'apixaban', 'elliquis', 'coumadin', 'apixa', 'warfarin'}
    pos_keywords = {'continue', 'start', 'restart' 'begin', 'use', 'remain', 'back to', 'will be on', 'resume', 'reverse', 'Chronic', 'recommended', 'recommending', 'started', 'bedtime', 'is on', 'mg', 'every day' }
    neg_keywords = {'discontinue', 'stop', 'hold', 'go off'}
    results_file = "extracted_results" + timestr + '.csv'

    # Find All Files
    files = glob.glob('*.txt')
    for f in files:
        # Loop through each file and match them

        with open(os.path.join(f), encoding='utf-8', errors='replace') as master_file:
            with open(results_file, "a+") as finalfile:
                writer = csv.writer(finalfile, delimiter='|')
                print('line')
                for line in master_file:
                    print('line')
                    line = re.sub(r'[^\x00-\x7F]+', ' ', line)

                    print(line)
                    if set(line.lower().split()[:-1]) & keywords_file:
                        click.echo('Found Match:: {}'.format(line))
                        matched_word = process.extract(
                            line, keywords_file, limit=1)
                        click.secho(
                            ('Match Word:: {}'.format(matched_word)), fg="yellow")

                        if set(line.lower().split()[:-1]) & pos_keywords:
                            click.secho(
                                ('Positive::{}'.format(line)), fg="blue")
                            label = "Positive"
                        elif set(line.lower().split()[:-1]) & neg_keywords:
                            click.secho(
                                ('Negative::{}'.format(line)), fg="red")
                            label = "Negative"
                        else:
                            label = 'Neutral'
                        result = '"Filename":"{}"|\n"Matched_Sentence":"{}"|\n"Label":"{}"\n'.format(
                            master_file.name, line, label)
                        print(result)
                        writer.writerow((f, line.strip(), label))
                        click.secho(
                            ('Finished Task For: {}'.format(line)), fg="blue")
                        click.secho(
                            ('Saved Result in File: {}'.format(results_file)), fg="blue")
                    elif set(line.lower().split()[:-1]) not in keywords_file:
                        click.secho(
                            ('None Found::{}'.format(line)), fg="green")

        click.secho(('Finished Task For: {}'.format(f)), fg="blue")
        click.secho(
            ('Saved Result in File: {}'.format(results_file)), fg="blue")


@main.command()
@click.argument('main_file')
@click.argument('keywords')
@click.argument('positive')
@click.argument('negative')
def matchfiles(main_file, keywords, positive, negative):
    """ Match File 1 with Keywords From 3 Files

    eg. matchtagger matchfiles masterfile.txt keywordfile.txt positivefile.txt negativefile.txt

    eg. python matchtagger matchfiles masterfile.txt keywordfile.txt positivefile.txt negativefile.txt

    """
    with open(os.path.join(keywords)) as second_file:
        keywords_file = set(second_file.read().lower().split())

    with open(os.path.join(positive)) as third_file:
        pos_keywords = set(third_file.read().lower().split())

    with open(os.path.join(negative)) as fourth_file:
        neg_keywords = set(fourth_file.read().lower().split())

    # File Name
    results_file = "extracted_results" + timestr + '.csv'

    # Open and Match Files
    with open(os.path.join(main_file), errors='replace') as master_file:
        with open(results_file, "a+") as finalfile:
            writer = csv.writer(finalfile, delimiter='|')
            for line in master_file:
                if set(line.lower().split()[:-1]) & keywords_file:
                    click.echo('Found Match:: {}'.format(line))
                    matched_word = process.extract(
                        line, keywords_file, limit=1)
                    click.secho(
                        ('Match Word:: {}'.format(matched_word)), fg="yellow")
                    if set(line.lower().split()[:-1]) & pos_keywords:
                        click.secho(('Positive::{}'.format(line)), fg="blue")
                        label = "Positive"
                    if set(line.lower().split()[:-1]) & neg_keywords:
                        click.secho(('Negative::{}'.format(line)), fg="red")
                        label = "Negative"

                    result = '"Filename":"{}"|\n"Matched_Sentence":"{}"|\n"Label":"{}"\n'.format(
                        master_file.name, line, label)
                    print(result)
                    writer.writerow(
                        (main_file, line.strip(), label))
                    click.secho(
                        ('Finished Task For: {}'.format(line)), fg="blue")
                    click.secho(
                        ('Saved Result in File: {}'.format(results_file)), fg="blue")

                elif set(line.lower().split()[:-1]) not in keywords_file:
                    click.secho(('None Found::{}'.format(line)), fg="green")
                else:
                    click.secho(('Neutral::{}'.format(line)), fg="green")
                    label = "Neutral"
    click.secho(('Saved Result in File: {}'.format(results_file)), fg="blue")


if __name__ == '__main__':
    main()
