#include "dialogsimulation.h"
#include "ui_dialogsimulation.h"

DialogSimulation::DialogSimulation(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogSimulation)
{
    ui->setupUi(this);
}

DialogSimulation::~DialogSimulation()
{
    delete ui;
}
