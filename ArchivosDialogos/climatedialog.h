#ifndef CLIMATEDIALOG_H
#define CLIMATEDIALOG_H

#include <QDialog>

namespace Ui {
class ClimateDialog;
}

class ClimateDialog : public QDialog
{
    Q_OBJECT

public:
    explicit ClimateDialog(QWidget *parent = nullptr);
    ~ClimateDialog();

private:
    Ui::ClimateDialog *ui;
};

#endif // CLIMATEDIALOG_H
