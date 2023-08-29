#include "controltopagnps.h"
#include "ui_controltopagnps.h"

ControlTOPAGNPS::ControlTOPAGNPS(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ControlTOPAGNPS)
{
    ui->setupUi(this);
}

ControlTOPAGNPS::~ControlTOPAGNPS()
{
    delete ui;
}
