#include "climatedialog.h"
#include "ui_climatedialog.h"

ClimateDialog::ClimateDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ClimateDialog)
{
    ui->setupUi(this);
}

ClimateDialog::~ClimateDialog()
{
    delete ui;
}
